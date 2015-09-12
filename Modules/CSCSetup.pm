package CSCSetup;


use strict;
use CGI::Carp qw(fatalsToBrowser);
#Create local Variable for use here only
# $datasourcetype = 'file';
my $datesourcetype = 'MySQL';
#my $datesourcetype = 'file';


sub new {
my $package   = shift;
my $UseModPerl = shift || 1;

# This is where you define your variable mapping.
my $self =  {-HOME_VIEW_NAME       => 'HomeView',
       -SITE_LAST_UPDATE           => 'October 6, 2011',
	    -HOME_VIEW                  => 'PageView',
	    -BASIC_DATA_VIEW            => 'BasicDataView',
 	    -ADDITIONALAUTHUSERNAMECOMMENTS => 'Please do not use spaces.',
	    -APP_LOGO                   => '/images/csc/cscbig.gif',
	    -APP_LOGO_ALT               => "CSC Logo, web development, CG, Perl, scripting, interactive, e-commerce, SSL,
                               cybercash, ibill, authorizenet, third party card processing, integration,
                               Selena Sol, WebWare, Webstore, Extropia, Devlopers, Network,
                               Unix, Linux, Apache, Modules, Sendmail, Majordomo, Monarch, SSH, BSD,
                               security, programming, webmaster, HTML, B.C., British, Columbia,
                               Canada, Canadian, Virtual, Server, Host, Development, Custom,
                               Scripting, Secure, Domain, Name, Registration, eComerce",
	    -APP_LOGO_WIDTH             => '150',
	    -APP_LOGO_HEIGHT            => '60',
	    -FAVICON                    => '/images/apis/favicon.ico',
	    -ANI_FAVICON                => '/images/apis/extra/animated_favicon.gif',
	    -FAVICON_TYPE               => '/image/x-icon',
	    -CSS_VIEW_NAME              => '/styles/CSCCSSView.css',
       -DEFAULT_CHARSET            => 'ISO-8859-1', 
	    -DOCUMENT_ROOT_URL          => '/',
	    -TEMPLATES_CACHE_DIRECTORY  => '/TemplatesCache',
	    -APP_DATAFILES_DIRECTORY    => "../../Datafiles/CSC",
	    -GLOBAL_DATAFILES_DIRECTORY => "../../Datafiles",
       -HTTP_HEADER_PARAMS         => "[-EXPIRES => '-1d']",
	    -IMAGE_ROOT_URL             => '/images/extropia',
       -LINK_TARGET                => '_self',
	    -MAIL_FROM                  => 'support@computersystemconsulting.ca',
	    -MAIL_TO                    => 'support@computersystemconsulting.ca',
	    -MAIL_TO_ADMIN              => 'support@computersystemconsulting.ca',
	    -MAIL_TO_USER               => 'csc_user_list@computersystemconsulting.ca',
	    -MAIL_TO_CLIENT             => 'csc_client@computersystemconsulting.ca',
	    -MAIL_REPLYTO               => 'csc@computersystemconsulting.ca',
	    -PAGE_TOP_VIEW              => 'PageTopView',
	    -PAGE_BOTTOM_VIEW           => 'PageBottomView',
	    -PAGE_LEFT_VIEW             => 'LeftPageView',
	    -LEFT_PAGE_VIEW             => 'LeftPageView',
 	    -SESSION_TIME_OUT           => 60 * 60 * 2,
 	    -SHOP	                    => "csc",
       -SITE_DISPLAY_NAME          => 'Computer System Consulting.ca',
       -AUTH_TABLE                 => 'csc_user_auth_tb',
       -ADMIN_AUTH_TABLE                 => 'csc_admin_auth_tb',
       -HAS_MEMBERS                => 1,
       -HTTP_HEADER_PARAMS         => "[-EXPIRES => '-1d']",
       -HTTP_HEADER_DESCRIPTION    => "Computer System Consulting.ca is dedicated to online applications using secure Linux/Unix systems. ",
       -HTTP_HEADER_KEYWORDS       => "web development, CGI, Perl, scripting, interactive, e-commerce, SSL, third party card processing, integration, PayPal, Selena Sol, WebWare, Webstore, Extropia, Devlopers, Network,
                                      Unix, Linux, Apache, Modules, Sendmail, Majordomo, security, programming, webmaster, HTML5, B.C., British Columbia,
                                      Canada, Canadian, Virtual, Server, Host, Development, Custom,Perl Scripting, Secure, Domain Name Registration, Hosting, Web appilcation hosting",
	    };

#return your variables to the application file.
return bless $self, $package; 
}

1;