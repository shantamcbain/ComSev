package BBS::DisplayDetailsRecordViewAction;

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
        -AUTH_MANAGER_CONFIG_PARAMS,
        -CGI_OBJECT,
        -DATASOURCE_CONFIG_PARAMS,
        -DETAILS_VIEW_NAME,
        -ENABLE_SORTING_FLAG,
        -KEY_FIELD,
        -LAST_RECORD_ON_PAGE,
        -MAX_RECORDS_PER_PAGE,
        -REQUIRE_AUTH_FOR_SEARCHING_FLAG,
        -REQUIRE_AUTH_FOR_VIEWING_DETAILS_FLAG,
        -REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG,
        -REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG,
        -SIMPLE_SEARCH_STRING,
        -SESSION_OBJECT,
        -SORT_DIRECTION,
        -SORT_FIELD1,
        -SORT_FIELD2,
        -DISPLAY_FIELDS,
        -FIELD_NAME_MAPPINGS,
            ],
            [
        -APPLICATION_OBJECT
            ],
        @_
    );

    my $app     = $params->{-APPLICATION_OBJECT};
    my $cgi     = $params->{-CGI_OBJECT};
    my $session = $params->{-SESSION_OBJECT};

    if (defined($cgi->param('display_details_view'))) {
        if ($params->{-REQUIRE_AUTH_FOR_VIEWING_DETAILS_FLAG}) {
            if ($params->{-AUTH_MANAGER_CONFIG_PARAMS}) {
                my $auth_manager = Extropia::Core::AuthManager->create(@{$params->{-AUTH_MANAGER_CONFIG_PARAMS}})
                   or die("Whoopsy!  I was unable to construct the " .
                           "Authentication object. " .
                           "Please contact the webmaster."
                );
                $auth_manager->authenticate();
            }
            else {
                die('You have set -REQUIRE_AUTH_FOR_VIEWING_DETAILS_FLAG to 1 ' .
                    'in the application executable, but you have not ' .
                    'defined -AUTH_MANAGER_CONFIG_PARAMS in the ' .
                    '@ACTION_HANDLER_ACTION_PARAMS array ' .
                    'in the application executable. This action ' .
                    'cannot procede unless you do both.'
                );
            }
        }

        if ($params->{-REQUIRE_AUTH_FOR_SEARCHING_FLAG}) {
            if ($params->{-AUTH_MANAGER_CONFIG_PARAMS}) {
                my $auth_manager = Extropia::Core::AuthManager->create(@{$params->{-AUTH_MANAGER_CONFIG_PARAMS}})
                   or die("Whoopsy!  I was unable to construct the " .
                           "Authentication object. " .
                           "Please contact the webmaster."
                );
                $auth_manager->authenticate();
            }

            else {
                die('You have set -REQUIRE_AUTH_FOR_SEARCHING_FLAG to 1 ' .
                    'in the application executable, but you have not ' .
                    'defined -AUTH_MANAGER_CONFIG_PARAMS in the ' .
                    '@ACTION_HANDLER_ACTION_PARAMS array ' .
                    'in the application executable. This action ' .
                    'cannot procede unless you do both.'
                );
            }
        }

        my @config_params = _rearrange([
            -BASIC_DATASOURCE_CONFIG_PARAMS
                ],
                [
            -BASIC_DATASOURCE_CONFIG_PARAMS
                ],
            @{$params->{-DATASOURCE_CONFIG_PARAMS}}
        );

        my $datasource_config_params = shift (@config_params);

        if ($datasource_config_params) {
            my ($ra_records) = $app->loadData((
                -ENABLE_SORTING_FLAG         => $params->{-ENABLE_SORTING_FLAG},
                -ALLOW_USERNAME_FIELD_TO_BE_SEARCHED => $params->{-ALLOW_USERNAME_FIELD_TO_BE_SEARCHED},
                -KEY_FIELD                   => $params->{-KEY_FIELD},
                -DATASOURCE_CONFIG_PARAMS    => $datasource_config_params,
                -SORT_DIRECTION              => $params->{-SORT_DIRECTION},
                -RECORD_ID                   => $cgi->param('record_id') || "",
                -SORT_FIELD1                 => $params->{-SORT_FIELD1},
                -SORT_FIELD2                 => $params->{-SORT_FIELD2},
                -MAX_RECORDS_PER_PAGE        => $params->{-MAX_RECORDS_PER_PAGE},
                -LAST_RECORD_ON_PAGE         => $params->{-LAST_RECORD_ON_PAGE},
                -SIMPLE_SEARCH_STRING        => $params->{-SIMPLE_SEARCH_STRING},
                -CGI_OBJECT                  => $params->{-CGI_OBJECT},
                -SESSION_OBJECT              => $params->{-SESSION_OBJECT},
                -REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG => $params->{-REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG},
                -REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG => $params->{-REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG}
            ));

            $app->setAdditionalViewDisplayParam
                (
                 -PARAM_NAME  => "-RECORDS",
                 -PARAM_VALUE => $ra_records,
                );

#            $record_set->moveFirst();
#            my $key_field = $params->{-KEY_FIELD};
#            my $record_id = $record_set->getField($key_field);
#print STDERR "record_id $record_id\n";
#            my $ra_default_display_fields = $params->{-DISPLAY_FIELDS};
#print STDERR "ra_default_display_fields @$ra_default_display_fields\n";
#            my $rh_field_name_mappings    = $params->{-FIELD_NAME_MAPPINGS};
#            my @fields_order = ();
#            my %record       = ();
#            foreach my $field (@$ra_default_display_fields) {
#                my $field_name = $rh_field_name_mappings->{$field} || $field;
#                push @fields_order, $field_name;
#                $record{$field_name} = $record_set->getField($field);
#            }

#            use Data::Dumper;
#            print STDERR Dumper \%record;

#            $app->setAdditionalViewDisplayParam(
#                -PARAM_NAME  => "-RECORD",
#                -PARAM_VALUE => \%record,
#            );

#            $app->setAdditionalViewDisplayParam(
#                -PARAM_NAME  => "-FIELDS_ORDER",
#                -PARAM_VALUE => \@fields_order,
#            );

            # Helper Functions
#          $app->setAdditionalViewDisplayParam(
#                -PARAM_NAME  => "-SUBS",
#                -PARAM_VALUE => {
#                                 'gmtime' => sub {scalar gmtime(shift)},
#                                }
#            );

            


        } else {
            die('You must specify a configuration for ' .
                '-BASIC_DATASOURCE_CONFIG_PARAMS in order to ' .
                'use loadData(). You may do so in the ' .
                '@ACTION_HANDLER_ACTION_PARAMS array ' .
                'in the application executable'
            );
        }

        $app->setNextViewToDisplay(
            -VIEW_NAME => $params->{-DETAILS_VIEW_NAME}
        );

        return 1;
    }

    return 0;
}
