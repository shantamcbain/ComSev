#============================================================= -*-Perl-*-
#
# Template::Plugins
#
# DESCRIPTION
#   Plugin provider which handles the loading of plugin modules and 
#   instantiation of plugin objects.
#
# AUTHORS
#   Andy Wardley <abw@kfs.org>
#
# COPYRIGHT
#   Copyright (C) 1996-2000 Andy Wardley.  All Rights Reserved.
#   Copyright (C) 1998-2000 Canon Research Centre Europe Ltd.
#
#   This module is free software; you can redistribute it and/or
#   modify it under the same terms as Perl itself.
#
#----------------------------------------------------------------------------
#
# $Id: Plugins.pm,v 1.3 2001/04/17 06:13:04 stas Exp $
#
#============================================================================

package Template::Plugins;

require 5.004;

use strict;
use base qw( Template::Base );
use vars qw( $VERSION $DEBUG $STD_PLUGINS );
use Template::Constants;

$VERSION = sprintf("%d.%02d", q$Revision: 1.3 $ =~ /(\d+)\.(\d+)/);

$STD_PLUGINS   = {
    'autoformat' => 'Template::Plugin::Autoformat',
    'cgi'        => 'Template::Plugin::CGI',
    'date'       => 'Template::Plugin::Date',
    'dbi'        => 'Template::Plugin::DBI',
    'url'        => 'Template::Plugin::URL',
    'pod'        => 'Template::Plugin::Pod',
    'format'     => 'Template::Plugin::Format',
    'table'      => 'Template::Plugin::Table',
    'iterator'   => 'Template::Plugin::Iterator',
    'datafile'   => 'Template::Plugin::Datafile',
    'dumper'     => 'Template::Plugin::Dumper',
    'view'       => 'Template::Plugin::View',
    'wrap'       => 'Template::Plugin::Wrap',
};


#========================================================================
#                         -- PUBLIC METHODS --
#========================================================================

#------------------------------------------------------------------------
# fetch($name, \@args, $context)
#
# General purpose method for requesting instantiation of a plugin
# object.  The name of the plugin is passed as the first parameter.
# The internal FACTORY lookup table is consulted to retrieve the
# appropriate factory object or class name.  If undefined, the _load()
# method is called to attempt to load the module and return a factory
# class/object which is then cached for subsequent use.  A reference
# to the calling context should be passed as the third parameter.
# This is passed to the _load() class method.  The new() method is
# then called against the factory class name or prototype object to
# instantiate a new plugin object, passing any arguments specified by
# list reference as the second parameter.  e.g. where $factory is the
# class name 'MyClass', the new() method is called as a class method,
# $factory->new(...), equivalent to MyClass->new(...) .  Where
# $factory is a prototype object, the new() method is called as an
# object method, $myobject->new(...).  This latter approach allows
# plugins to act as Singletons, cache shared data, etc.  
#
# Returns a reference to a plugin, (undef, STATUS_DECLINE) to decline
# the request or ($error, STATUS_ERROR) on error.
#------------------------------------------------------------------------

sub fetch {
    my ($self, $name, $args, $context) = @_;
    my ($factory, $plugin, $error);

    # NOTE:
    # the $context ref gets passed as the first parameter to all regular
    # plugins, but not to those loaded via LOAD_PERL;  to hack around
    # this until we have a better implementation, we pass the $args
    # reference to _load() and let it unshift the first args in the 
    # LOAD_PERL case

    $args ||= [ ];
    unshift @$args, $context;

    $factory = $self->{ FACTORY }->{ $name } ||= do {
	($factory, $error) = $self->_load($name, $args);
	return ($factory, $error) if $error;			## RETURN
	$factory;
    };

    # call the new() method on the factory object or class name
    eval {
	print STDERR "args: [ @$args ]\n"
	    if $DEBUG;
	$plugin = $factory->new(@$args)
    	    || die "$name plugin failed: ", $factory->error(), "\n";	## DIE
    };
    if ($error = $@) {
#	chomp $error;
	return $self->{ TOLERANT } 
	       ? (undef,  Template::Constants::STATUS_DECLINED)
	       : ($error, Template::Constants::STATUS_ERROR);
    }

    return $plugin;
}



#========================================================================
#                        -- PRIVATE METHODS --
#========================================================================

#------------------------------------------------------------------------
# _init(\%config)
#
# Private initialisation method.
#------------------------------------------------------------------------

sub _init {
    my ($self, $params) = @_;
    my ($pbase, $plugins, $factory) = 
	@$params{ qw( PLUGIN_BASE PLUGINS PLUGIN_FACTORY ) };

    $plugins ||= { };
    if (ref $pbase ne 'ARRAY') {
	$pbase = $pbase ? [ $pbase ] : [ ];
    }
    push(@$pbase, 'Template::Plugin');

    $self->{ PLUGIN_BASE } = $pbase;
    $self->{ PLUGINS     } = { %$STD_PLUGINS, %$plugins };
    $self->{ TOLERANT    } = $params->{ TOLERANT }  || 0;
    $self->{ LOAD_PERL   } = $params->{ LOAD_PERL } || 0;
    $self->{ FACTORY     } = $factory || { };

    return $self;
}



#------------------------------------------------------------------------
# _load($name, $args)
#
# Private method which attempts to load a plugin module and determine the 
# correct factory name or object by calling the load() class method in
# the loaded module.
#------------------------------------------------------------------------

sub _load {
    my ($self, $name, $args) = @_;
    my ($factory, $module, $base, $pkg, $file, $ok, $error);

    if ($module = $self->{ PLUGINS }->{ $name }) {
	# plugin module name is explicitly stated in PLUGIN_NAME
	$pkg = $module;
	($file = $module) =~ s|::|/|g;
	$file =~ s|::|/|g;
	print STDERR "fetch() loading $module.pm (PLUGIN_NAME)\n"
	    if $DEBUG;
	$ok = eval { require "$file.pm" };
	$error = $@;
    }
    else {
	# try each of the PLUGIN_BASE values to build module name
	($module = $name) =~ s/\./::/g;

	foreach $base (@{ $self->{ PLUGIN_BASE } }) {
	    $pkg = $base . '::' . $module;
	    ($file = $pkg) =~ s|::|/|g;

	    print STDERR "fetch() attempting to load $file.pm (PLUGIN_BASE)\n"
		if $DEBUG;

	    $ok = eval { require "$file.pm" };
	    last unless $@;
	
	    $error .= "$@\n" 
		unless ($@ =~ /^Can\'t locate $file\.pm/);
	}
    }

    if ($ok) {
	print STDERR "fetch() attempting to call $pkg->load()\n"
	    if $DEBUG;

	# first item in @$args is context reference, passed to load()
	$factory = eval { $pkg->load($args->[0]) };
	$error   = '';
	if ($@ || ! $factory) {
	    $error = $@ || 'load() returned a false value';
	}
    }
    elsif ($self->{ LOAD_PERL }) {
	# fallback - is it a regular Perl module?
	($file = $module) =~ s|::|/|g;
	eval { require "$file.pm" };
	if ($@) {
	    $error = $@;
	}
	else {
	    # remove the context reference from the args list - this isn't
	    # a plugin module and won't be expecting it
	    shift(@$args);
	    $factory = $module;
	    $error   = '';
	}
    }

    if ($factory) {
	print STDERR "load($name) => $factory\n"
	    if $DEBUG;
	return $factory;
    }
    elsif ($error) {
	return $self->{ TOLERANT } 
	    ? (undef,  Template::Constants::STATUS_DECLINED) 
	    : ($error, Template::Constants::STATUS_ERROR);
    }
    else {
	return (undef, Template::Constants::STATUS_DECLINED);
    }
}


#------------------------------------------------------------------------
# _dump()
# 
# Debug method which constructs and returns text representing the current
# state of the object.
#------------------------------------------------------------------------

sub _dump {
    my $self = shift;
    local $" = ', ';
    my $fkeys = join(", ", keys %{$self->{ FACTORY }});
    my $plugins = $self->{ PLUGINS };
    $plugins = join(", ", map { "$_ => $plugins->{ $_ }" } keys %$plugins);

    return <<EOF;
$self
PLUGIN_BASE => [ @{ $self->{ PLUGIN_BASE } } ]
PLUGINS     => { $plugins }
FACTORY     => [ $fkeys ]
TOLERANT    => $self->{ TOLERANT }
LOAD_PERL   => $self->{ LOAD_PERL }
EOF
}


1;

__END__


#------------------------------------------------------------------------
# IMPORTANT NOTE
#   This documentation is generated automatically from source
#   templates.  Any changes you make here may be lost.
# 
#   The 'docsrc' documentation source bundle is available for download
#   from http://www.template-toolkit.org/docs.html and contains all
#   the source templates, XML files, scripts, etc., from which the
#   documentation for the Template Toolkit is built.
#------------------------------------------------------------------------

=head1 NAME

Template::Plugins - Plugin provider module

=head1 SYNOPSIS

    use Template::Plugins;

    $plugin_provider = Template::Plugins->new(\%options);

    ($plugin, $error) = $plugin_provider->fetch($name, @args);

=head1 DESCRIPTION

The Template::Plugins module defines a provider class which can be used
to load and instantiate Template Toolkit plugin modules.

=head1 METHODS

=head2 new(\%params) 

Constructor method which instantiates and returns a reference to a
Template::Plugins object.  A reference to a hash array of configuration
items may be passed as a parameter.  These are described below.  

Note that the Template.pm front-end module creates a Template::Plugins
provider, passing all configuration items.  Thus, the examples shown
below in the form:

    $plugprov = Template::Plugins->new({
	PLUGIN_BASE => 'MyTemplate::Plugin',
        LOAD_PERL   => 1,
	...
    });

can also be used via the Template module as:

    $ttengine = Template->new({
	PLUGIN_BASE => 'MyTemplate::Plugin',
        LOAD_PERL   => 1,
	...
    });

as well as the more explicit form of:

    $plugprov = Template::Plugins->new({
	PLUGIN_BASE => 'MyTemplate::Plugin',
        LOAD_PERL   => 1,
	...
    });

    $ttengine = Template->new({
	LOAD_PLUGINS => [ $plugprov ],
    });

=head2 fetch($name, @args)

Called to request that a plugin of a given name be provided.  The relevant 
module is first loaded (if necessary) and the load() class method called 
to return the factory class name (usually the same package name) or a 
factory object (a prototype).  The new() method is then called as a 
class or object method against the factory, passing all remaining
parameters.

Returns a reference to a new plugin object or ($error, STATUS_ERROR)
on error.  May also return (undef, STATUS_DECLINED) to decline to
serve the request.  If TOLERANT is set then all errors will be
returned as declines.

=head1 CONFIGURATION OPTIONS

The following list details the configuration options that can be provided
to the Template::Plugins new() constructor.

=over 4




=item PLUGINS

The PLUGINS options can be used to provide a reference to a hash array
that maps plugin names to Perl module names.  A number of standard
plugins are defined (e.g. 'table', 'cgi', 'dbi', etc.) which map to
their corresponding Template::Plugin::* counterparts.  These can be
redefined by values in the PLUGINS hash.

    my $plugins = Template::Plugins->new({
	PLUGINS => {
	    cgi => 'MyOrg::Template::Plugin::CGI',
    	    foo => 'MyOrg::Template::Plugin::Foo',
	    bar => 'MyOrg::Template::Plugin::Bar',
	},
    });

The USE directive is used to create plugin objects and does so by
calling the plugin() method on the current Template::Context object.
If the plugin name is defined in the PLUGINS hash then the
corresponding Perl module is loaded via require().  The context then
calls the load() class method which should return the class name 
(default and general case) or a prototype object against which the 
new() method can be called to instantiate individual plugin objects.

If the plugin name is not defined in the PLUGINS hash then the PLUGIN_BASE
and/or LOAD_PERL options come into effect.





=item PLUGIN_BASE

If a plugin is not defined in the PLUGINS hash then the PLUGIN_BASE is used
to attempt to construct a correct Perl module name which can be successfully 
loaded.  

The PLUGIN_BASE can be specified as a single value or as a reference
to an array of multiple values.  The default PLUGIN_BASE value,
'Template::Plugin', is always added the the end of the PLUGIN_BASE
list (a single value is first converted to a list).  Each value should
contain a Perl package name to which the requested plugin name is
appended.

example 1:

    my $plugins = Template::Plugins->new({
	PLUGIN_BASE => 'MyOrg::Template::Plugin',
    });

    [% USE Foo %]    # => MyOrg::Template::Plugin::Foo
                       or        Template::Plugin::Foo 

example 2:

    my $plugins = Template::Plugins->new({
	PLUGIN_BASE => [   'MyOrg::Template::Plugin',
			 'YourOrg::Template::Plugin'  ],
    });

    [% USE Foo %]    # =>   MyOrg::Template::Plugin::Foo
                       or YourOrg::Template::Plugin::Foo 
                       or          Template::Plugin::Foo 






=item LOAD_PERL

If a plugin cannot be loaded using the PLUGINS or PLUGIN_BASE
approaches then the provider can make a final attempt to load the
module without prepending any prefix to the module path.  This allows
regular Perl modules (i.e. those that don't reside in the
Template::Plugin or some other such namespace) to be loaded and used
as plugins.

By default, the LOAD_PERL option is set to 0 and no attempt will be made
to load any Perl modules that aren't named explicitly in the PLUGINS
hash or reside in a package as named by one of the PLUGIN_BASE
components.  

Plugins loaded using the PLUGINS or PLUGIN_BASE receive a reference to
the current context object as the first argument to the new()
constructor.  Modules loaded using LOAD_PERL are assumed to not
conform to the plugin interface.  They must provide a new() class
method for instantiating objects but it will not receive a reference
to the context as the first argument.  Plugin modules should provide a
load() class method (or inherit the default one from the
Template::Plugin base class) which is called the first time the plugin
is loaded.  Regular Perl modules need not.  In all other respects,
regular Perl objects and Template Toolkit plugins are identical.

If a particular Perl module does not conform to the common, but not
unilateral, new() constructor convention then a simple plugin wrapper
can be written to interface to it.




=item TOLERANT

The TOLERANT flag is used by the various Template Toolkit provider
modules (Template::Provider, Template::Plugins, Template::Filters) to
control their behaviour when errors are encountered.  By default, any
errors are reported as such, with the request for the particular
resource (template, plugin, filter) being denied and an exception
raised.  When the TOLERANT flag is set to any true values, errors will
be silently ignored and the provider will instead return
STATUS_DECLINED.  This allows a subsequent provider to take
responsibility for providing the resource, rather than failing the
request outright.  If all providers decline to service the request,
either through tolerated failure or a genuine disinclination to
comply, then a 'E<lt>resourceE<gt> not found' exception is raised.




=back



=head1 TEMPLATE TOOLKIT PLUGINS

The following plugin modules are distributed with the Template
Toolkit.  Some of the plugins interface to external modules (detailed
below) which should be downloaded from any CPAN site and installed
before using the plugin.

=over 4

=item Autoformat

The Autoformat plugin is an interface to Damian Conway's Text::Autoformat 
Perl module which provides advanced text wrapping and formatting.  See
L<Template::Plugin::Autoformat> and L<Text::Autoformat> for further 
details.

    [% USE autoformat(left=10, right=20) %]
    [% autoformat(mytext) %]	    # call autoformat sub
    [% mytext FILTER autoformat %]  # or use autoformat filter

The Text::Autoformat module is available from CPAN:

    http://www.cpan.org/modules/by-module/Text/

=item CGI

The CGI plugin is a wrapper around Lincoln Stein's 
E<lt>lstein@genome.wi.mit.eduE<gt> CGI.pm module.  The plugin is 
distributed with the Template Toolkit (see L<Template::Plugin::CGI>)
and the CGI module itself is distributed with recent versions Perl,
or is available from CPAN.

    [% USE CGI %]
    [% CGI.param('param_name') %]
    [% CGI.start_form %]
    [% CGI.popup_menu( Name   => 'color', 
                       Values => [ 'Green', 'Brown' ] ) %]
    [% CGI.end_form %]

=item Datafile

Provides an interface to data stored in a plain text file in a simple
delimited format.  The first line in the file specifies field names
which should be delimiter by any non-word character sequence.
Subsequent lines define data using the same delimiter as int he first
line.  Blank lines and comments (lines starting '#') are ignored.  See
L<Template::Plugin::Datafile> for further details.

/tmp/mydata:

    # define names for each field
    id : email : name : tel
    # here's the data
    fred : fred@here.com : Fred Smith : 555-1234
    bill : bill@here.com : Bill White : 555-5678

example:

    [% USE userlist = datafile('/tmp/mydata') %]

    [% FOREACH user = userlist %]
       [% user.name %] ([% user.id %])
    [% END %]

=item Date

The Date plugin provides an easy way to generate formatted time and date
strings by delegating to the POSIX strftime() routine.   See
L<Template::Plugin::Date> and L<POSIX> for further details.

    [% USE date %]
    [% date.format %]		# current time/date

    File last modified: [% date.format(template.modtime) %]

=item DBI

The DBI plugin, developed by Simon Matthews
E<lt>sam@knowledgepool.comE<gt>, brings the full power of Tim Bunce's
E<lt>Tim.Bunce@ig.co.ukE<gt> database interface module (DBI) to your
templates.  See L<Template::Plugin::DBI> and L<DBI> for further details.

    [% USE DBI('dbi:driver:database', 'user', 'pass') %]

    [% FOREACH user = DBI.query( 'SELECT * FROM users' ) %]
       [% user.id %] [% user.name %]
    [% END %]

The DBI and relevant DBD modules are available from CPAN:

  http://www.cpan.org/modules/by-module/DBI/

=item Dumper

The Dumper plugin provides an interface to the Data::Dumper module.  See
L<Template::Plugin::Dumper> and L<Data::Dumper> for futher details.

    [% USE dumper(indent=0, pad="<br>") %]
    [% dumper.dump(myvar, yourvar) %]

=item Format

The Format plugin provides a simple way to format text according to a
printf()-like format.   See L<Template::Plugin::Format> for further 
details.

    [% USE bold = format('<b>%s</b>') %]
    [% bold('Hello') %]

=item Iterator

The Iterator plugin provides a way to create a Template::Iterator
object to iterate over a data set.  An iterator is created
automatically by the FOREACH directive and is aliased to the 'loop'
variable.  This plugin allows an iterator to be explicitly created
with a given name, or the default plugin name, 'iterator'.  See
L<Template::Plugin::Iterator> for further details.

    [% USE iterator(list, args) %]

    [% FOREACH item = iterator %]
       [% '<ul>' IF iterator.first %]
       <li>[% item %]
       [% '</ul>' IF iterator.last %]
    [% END %]

=item Table

The Table plugin allows you to format a list of data items into a 
virtual table by specifying a fixed number of rows or columns, with 
an optional overlap.  See L<Template::Plugin::Table> for further 
details.

    [% USE table(list, rows=10, overlap=1) %]

    [% FOREACH item = table.col(3) %]
       [% item %]
    [% END %]

=item URL

The URL plugin provides a simple way of contructing URLs from a base
part and a variable set of parameters.  See L<Template::Plugin::URL>
for further details.

    [% USE mycgi = url('/cgi-bin/bar.pl', debug=1) %]

    [% mycgi %]
       # ==> /cgi/bin/bar.pl?debug=1

    [% mycgi(mode='submit') %]
       # ==> /cgi/bin/bar.pl?mode=submit&debug=1

=item Wrap

The Wrap plugin uses the Text::Wrap module by David Muir Sharnoff 
E<lt>muir@idiom.comE<gt> (with help from Tim Pierce and many many others)
to provide simple paragraph formatting.  See L<Template::Plugin::Wrap>
and L<Text::Wrap> for further details.

    [% USE wrap %]
    [% wrap(mytext, 40, '* ', '  ') %]	# use wrap sub
    [% mytext FILTER wrap(40) -%]	# or wrap FILTER

The Text::Wrap module is available from CPAN:

    http://www.cpan.org/modules/by-module/Text/

=item XML::DOM

The XML::DOM plugin gives access to the XML Document Object Module via
Clark Cooper E<lt>cooper@sch.ge.comE<gt> and Enno Derksen's 
E<lt>enno@att.comE<gt> XML::DOM module.  See L<Template::Plugin::XML::DOM> 
and L<XML::DOM> for further details.

    [% USE dom = XML.DOM %]
    [% doc = dom.parse(filename) %]

    [% FOREACH node = doc.getElementsByTagName('CODEBASE') %]
       * [% node.getAttribute('href') %]
    [% END %]

The plugin requires the XML::DOM module, available from CPAN:

    http://www.cpan.org/modules/by-module/XML/

=item XML::XPath

The XML::XPath plugin provides an interface to Matt Sergeant's
E<lt>matt@sergeant.orgE<gt> XML::XPath module.  See 
L<Template::Plugin::XML::XPath> and L<XML::XPath> for further details.

    [% USE xpath = XML.XPath(xmlfile) %]
    [% FOREACH page = xpath.findnodes('/html/body/page') %]
       [% page.getAttribute('title') %]
    [% END %]

The plugin requires the XML::XPath module, available from CPAN:

    http://www.cpan.org/modules/by-module/XML/

=item XML::RSS

The XML::RSS plugin is a simple interface to Jonathan Eisenzopf's
E<lt>eisen@pobox.comE<gt> XML::RSS module.  A RSS (Rich Site Summary)
file is typically used to store short news 'headlines' describing
different links within a site.  This plugin allows you to parse RSS
files and format the contents accordingly using templates.  
See L<Template::Plugin::XML::RSS> and L<XML::RSS> for further details.

    [% USE news = XML.RSS(filename) %]
   
    [% FOREACH item = news.items %]
       <a href="[% item.link %]">[% item.title %]</a>
    [% END %]

The XML::RSS module is available from CPAN:

    http://www.cpan.org/modules/by-module/XML/

=back



=head1 BUGS / ISSUES

=over 4

=item *

It might be worthwhile being able to distinguish between absolute
module names and those which should be applied relative to PLUGIN_BASE
directories.  For example, use 'MyNamespace::MyModule' to denote
absolute module names (e.g. LOAD_PERL), and 'MyNamespace.MyModule' to
denote relative to PLUGIN_BASE.

=back

=head1 AUTHOR

Andy Wardley E<lt>abw@kfs.orgE<gt>

L<http://www.andywardley.com/|http://www.andywardley.com/>

=head1 VERSION

2.12, distributed as part of the
Template Toolkit version 2.02, released on 06 April 2001.

=head1 COPYRIGHT

  Copyright (C) 1996-2001 Andy Wardley.  All Rights Reserved.
  Copyright (C) 1998-2001 Canon Research Centre Europe Ltd.

This module is free software; you can redistribute it and/or
modify it under the same terms as Perl itself.

=head1 SEE ALSO

L<Template|Template>, L<Template::Plugin|Template::Plugin>, L<Template::Context|Template::Context>


