package Default::PopulateInputWidgetDefinitionListWithApisWidgetAction;
# 	$Id: PopulateInputWidgetDefinitionListWithApisWidgetAction.pm,v 1.1 2004/01/25 03:41:44 shanta Exp shanta $	
#location /cgi-bin/ActionHandler/CSC

# Copyright (C) 1994 - 2001  eXtropia.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA  02111-1307, USA.

use strict;
use Extropia::Core::Base qw(_rearrange _rearrangeAsHash);
use Extropia::Core::Action;

use vars qw(@ISA);
@ISA = qw(Extropia::Core::Action);

sub execute {
    my $self = shift;
    my ($params) = _rearrangeAsHash([
        -ALLOW_USERNAME_FIELD_TO_BE_SEARCHED,
        -APPLICATION_OBJECT,
        -CGI_OBJECT,
        -DATASOURCE_CONFIG_PARAMS,
        -ENABLE_SORTING_FLAG,
        -KEY_FIELD,
        -LAST_RECORD_ON_PAGE,
        -MAX_RECORDS_PER_PAGE,
        -RECORD_ID,
        -REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG,
        -REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG,
        -REQUIRE_MATCHING_SITE_FOR_SEARCHING_FLAG,
        -SESSION_OBJECT,
        -SIMPLE_SEARCH_STRING,
        -SITE_NAME,
        -APP_NAME,
        -MOD_NAME,
        -SORT_DIRECTION,
        -SORT_FIELD1,
        -SORT_FIELD2,
        -VIEW_DISPLAY_PARAMS,
        -INPUT_WIDGET_DEFINITIONS,
            ],
            [
        -APPLICATION_OBJECT,
            ],
        @_
    );
#and  group_of_poster==$group    

my $app = $params->{-APPLICATION_OBJECT};

    my $cgi = $params->{-CGI_OBJECT};
my $SESSION    = $params->{-SESSION_OBJECT};
my $username =  $SESSION ->getAttribute(-KEY => 'auth_username');
my $group    =  $SESSION ->getAttribute('auth_groups');#||'Apis_admin';
my $sitename    =  $SESSION ->getAttribute('SiteName');#||'Apis_admin';

    $cgi->param(
        -NAME  => 'raw_search', 
        -VALUE => "status=='active' AND sitename=='Apis'  AND app_name == 'herbs'  AND list_name=='Apis'  
 "
    );   

    my @config_params = _rearrange([
        -DROPLIST_DATASOURCE_CONFIG_PARAMS
            ],
            [
        -DROPLIST_DATASOURCE_CONFIG_PARAMS
            ],
        @{$params->{-DATASOURCE_CONFIG_PARAMS}}
    );

#define tb to pick up info from


    my $datasource_config_params = shift (@config_params);

 #   my $datasource_config_params = shift @DATASOURCE_CONFIG_PARAMS;

    my $ra_records = $app->loadData((
        -ENABLE_SORTING_FLAG         => $params->{-ENABLE_SORTING_FLAG},
        -ALLOW_USERNAME_FIELD_TO_BE_SEARCHED => $params->{-ALLOW_USERNAME_FIELD_TO_BE_SEARCHED},
        -KEY_FIELD                   => $params->{-KEY_FIELD},
        -DATASOURCE_CONFIG_PARAMS    => $datasource_config_params,
        -SORT_DIRECTION              => $params->{-SORT_DIRECTION}|| 'ASC',
        -SORT_FIELD1                 => 'category',
        -SORT_FIELD2                 => '',
        -MAX_RECORDS_PER_PAGE        => $params->{-MAX_RECORDS_PER_PAGE},
        -LAST_RECORD_ON_PAGE         => $params->{-LAST_RECORD_ON_PAGE},
        -SIMPLE_SEARCH_STRING        => $params->{-SIMPLE_SEARCH_STRING},
        -CGI_OBJECT                  => $params->{-CGI_OBJECT},
        -SESSION_OBJECT              => $params->{-SESSION_OBJECT},
        -REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG => $params->{-REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG},
        -REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG => $params->{-REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG},
        -REQUIRE_MATCHING_SITE_FOR_SEARCHING_FLAG => $params->{-REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG},
    ));

    my @project_code;
    foreach my $record (@$ra_records) {
        my $username = $record->{'category'};
        push (@project_code, $username);
    }

    my @labels;
    foreach my $record (@$ra_records) {
        my $displayvalue = $record->{'display_value'};
        my $subject = $record->{'categorys'};
        push (@labels,$subject => $displayvalue);
    }
    my %labels = @labels;
#$labels{$values[$a]} = '$label';
    my @view_display_params = @{$params->{-VIEW_DISPLAY_PARAMS}};

    my $input_widget_config = $params->{-INPUT_WIDGET_DEFINITIONS};
    my @input_widget_config_params = _rearrange([
        -BASIC_INPUT_WIDGET_DEFINITIONS,
            ],
            [
        -BASIC_INPUT_WIDGET_DEFINITIONS,
            ],
        @$input_widget_config
    );

    my $input_widget_definitions = shift (@input_widget_config_params);
    my $addlink = "\<a href=\'http://computersystemconsulting.ca/cgi-bin/CSC/csc_url_sub.cgi?display_add_form=on\'\> ADD\</font\>\</a\>";
if ($params->{-APP_NAME} eq'faqsl_manager'){
     $addlink='Droplist admin adds new values';
}elsif ($params->{-APP_NAME} eq'treatment'){
 $addlink='Use Droplist to add contents';
}else{
 $addlink='';
}

    my @project_code_widget = (
        -DISPLAY_NAME => "Bee forage or indicator",
        -TYPE         => 'checkbox_group',
        -NAME         => 'apis',
	-size=>5,
        -VALUES       => \@project_code,
        -LABELS       => \%labels
   );
#        -LABELS       => \@labels

    $$input_widget_definitions{'apis'} = \@project_code_widget;

    my @new_value = (
        -BASIC_INPUT_WIDGET_DEFINITIONS => $input_widget_definitions
    );

    push (@input_widget_config_params, @new_value);

    $app->{-VIEW_DISPLAY_PARAMS}= $params->{-VIEW_DISPLAY_PARAMS};    

    $cgi->param(
        -NAME  => 'raw_search',
        -VALUE => ""
    );

    return 2;
}
