package Default::ProcessAddRequestAction;

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
        -ADD_ACKNOWLEDGEMENT_VIEW_NAME,
        -ADD_FORM_VIEW_NAME,
        -ALLOW_ADDITIONS_FLAG,
        -ALLOW_DUPLICATE_ENTRIES,
        -APPLICATION_OBJECT,
        -AUTH_MANAGER_CONFIG_PARAMS,
        -CGI_OBJECT,
        -DATA_HANDLER_MANAGER_CONFIG_PARAMS,
        -DATASOURCE_CONFIG_PARAMS,
        -DISPLAY_ACKNOWLEDGEMENT_ON_ADD_FLAG,
        -ADD_EMAIL_BODY_VIEW,
        -INPUT_WIDGET_DEFINITIONS,
        -KEY_FIELD,
        -LOG_CONFIG_PARAMS,
        -MAIL_CONFIG_PARAMS,
        -MAIL_SEND_PARAMS,
        -REQUIRE_AUTH_FOR_ADDING_FLAG,
        -SEND_EMAIL_ON_ADD_FLAG,
        -SESSION_OBJECT,
        -VIEW_DISPLAY_PARAMS,
        -VIEW_LOADER,
        -ACTION_HANDLER_PLUGINS,
        -POSTED_DATE
            ],
            [
        -ADD_FORM_VIEW_NAME,
        -APPLICATION_OBJECT,
        -CGI_OBJECT,
        -DATASOURCE_CONFIG_PARAMS,
        -KEY_FIELD
            ],
        @_
    );

    my $app                 = $params->{-APPLICATION_OBJECT};
    my $session             = $params->{-SESSION_OBJECT};
    my $cgi                 = $params->{-CGI_OBJECT};
    my $input_widget_config = $params->{-INPUT_WIDGET_DEFINITIONS};

    if (defined($cgi->param('submit_add_record'))) {
    	
        if (!$params->{-ALLOW_ADDITIONS_FLAG}) {
            die ('Sorry, but you are not allowed to perform additions. ' .
                 'To enable additions, you must set -ALLOW_ADDITIONS_FLAG ' .
                 'in the @ACTION_HANDLER_ACTION_PARAMS array ' .
                 'in the application executable to 1'
            );
        }

        if ($params->{-REQUIRE_AUTH_FOR_ADDING_FLAG}) {
            if ($params->{-AUTH_MANAGER_CONFIG_PARAMS}) {
                my $auth_manager = Extropia::Core::AuthManager->create(@{$params->{-AUTH_MANAGER_CONFIG_PARAMS}})
                    or die("Whoopsy!  I was unable to construct the " .
                           "Authentication object. " .
                           "Please contact the webmaster.");
                $auth_manager->authenticate();
            }
            else {
                die('You have set -REQUIRE_AUTH_FOR_ADDING_FLAG to 1 ' .
                    ' in the application executable, but you have not ' .
                    ' defined -AUTH_MANAGER_CONFIG_PARAMS in the ' .
                    '@ACTION_HANDLER_ACTION_PARAMS array ' .
                    'in the application executable. This action ' .
                    ' cannot procede unless you do both.'
                );
            }
        }

        my $log_object;
        if ($params->{'-LOG_CONFIG_PARAMS'}) {
             $log_object = Extropia::Core::Log->create(@{$params->{-LOG_CONFIG_PARAMS}})
                or die("Whoopsy!  I was unable to construct the " .
                       "Log object. Please " .
                       "contact the webmaster."
            );
        }

        my @dhm_config_params = _rearrange([
            -ADD_FORM_DHM_CONFIG_PARAMS
               ],
               [
               ],
            @{$params->{-DATA_HANDLER_MANAGER_CONFIG_PARAMS}}
         );

        my $add_form_dhm_config_params = shift (@dhm_config_params);

        my @input_widget_config_params = _rearrange([
                -BASIC_INPUT_WIDGET_DEFINITIONS,
                -BASIC_INPUT_WIDGET_DISPLAY_ORDER
                    ],
                    [
                -BASIC_INPUT_WIDGET_DEFINITIONS,
                -BASIC_INPUT_WIDGET_DISPLAY_ORDER
                    ],
                @$input_widget_config
        );

        my $input_widget_definitions   = shift (@input_widget_config_params);
        my $input_widget_display_order = shift (@input_widget_config_params);

        if ($add_form_dhm_config_params) {

            my $data_handler_success = $app->handleIncomingData(
                -CGI_OBJECT                 => $cgi,
                -LOG_OBJECT                 => $log_object,
                -DATA_HANDLER_CONFIG_PARAMS => $add_form_dhm_config_params,
                -ACTION_HANDLER_PLUGINS     => $params->{-ACTION_HANDLER_PLUGINS},
            );

            unless ($data_handler_success) {

                $app->setNextViewToDisplay(
                    -VIEW_NAME => $params->{-ADD_FORM_VIEW_NAME}
                );
                my $error;
                foreach $error ($app->getDataHandlerErrors()) {
                    $app->addError($error);
                }


               if (!$input_widget_display_order){
                   die('You have not defined -BASIC_INPUT_WIDGET_DISPLAY_ORDER ' .
                       'in the  @ACTION_HANDLER_ACTION_PARAMS array ' .
                       'in the application executable. This action ' .
                       'cannot procede unless you do so.'
                   );
               }

               if (!$input_widget_definitions){
                   die('You have not defined -BASIC_INPUT_WIDGET_DEFINITIONS ' .
                       'in the  @ACTION_HANDLER_ACTION_PARAMS array ' .
                       'in the application executable. This action ' .
                       'cannot procede unless you do so.'
                   );
               }

               $app->setAdditionalViewDisplayParam(
                   -PARAM_NAME => '-INPUT_WIDGET_CONFIG',
                   -PARAM_VALUE => $input_widget_definitions
               );

               $app->setAdditionalViewDisplayParam(
                   -PARAM_NAME => '-INPUT_WIDGET_DISPLAY_ORDER',
                   -PARAM_VALUE => $input_widget_display_order
               );

                return 1;
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
            my $addition_request_success = $app->addRecord((
                -CGI_OBJECT               => $params->{-CGI_OBJECT},
                -SESSION_OBJECT           => $params->{-SESSION_OBJECT},
                -KEY_FIELD                => $params->{-KEY_FIELD},
                -LOG_OBJECT               => $log_object,
                -DATASOURCE_CONFIG_PARAMS => $datasource_config_params,
                -ALLOW_DUPLICATE_ENTRIES  => $params->{-ALLOW_DUPLICATE_ENTRIES},
                -POSTED_DATE		  => $params->{-POSTED_DATE}||'',
            ));


           if ($addition_request_success) {
                if ($params->{-SEND_EMAIL_ON_ADD_FLAG}) {
                    my @send_params = _rearrange([
                        -ADD_EVENT_MAIL_SEND_PARAMS
                            ],
                            [
                            ],
                        @{$params->{-MAIL_SEND_PARAMS}}
                    );

                    my $mail_send_params = shift (@send_params);
                    
                    if (!$mail_send_params) {
                        die('You have not specified ' .
                            '-ADD_EVENT_MAIL_SEND_PARAMS in ' .
                            '@ACTION_HANDLER_ACTION_PARAMS array ' .
                            'in the application executable. ' .
                            'Please do so.'
                        );
                    }

                    if (!$params->{-ADD_EMAIL_BODY_VIEW}) {
                        die('You have not specified ' .
                            '-ADD_EMAIL_BODY_VIEW in ' .
                            '@ACTION_HANDLER_ACTION_PARAMS array ' .
                            'in the application executable. ' .
                            'Please do so.'
                        );
                    }

                    if (!$params->{-MAIL_CONFIG_PARAMS}) {
                        die('You have not specified ' .
                            '-MAIL_CONFIG_PARAMS in ' .
                            '@ACTION_HANDLER_ACTION_PARAMS array ' .
                            'in the application executable. ' .
                            'Please do so.'
                        );
                    }

                    my $view_loader = $params->{-VIEW_LOADER};
		    my $body = $view_loader->process_email
		    (
		    	$params->{-ADD_EMAIL_BODY_VIEW},
		    	{
		    		-CGI_OBJECT => $params->{-CGI_OBJECT},
		    		@_,
		    	}
		    );
            
            	  $app->runPlugins
            	  (
             		-ACTION_HANDLER_PLUGINS => $params->{-ACTION_HANDLER_PLUGINS},
            		-CATEGORY               => '-BeforeEmail',
            	  );
            	  
            	  my @others_mail_send_params  = _rearrange([
                            -SUBJECT
                                ],
                                [
                                ],
                                @$mail_send_params
                                );
                                
                   my $subject = shift(@others_mail_send_params);
                   
                   if($cgi->param('override_subject')) {
            	   	$subject .= ' - ' . $cgi->param('override_subject');
            	   }
            	   
                   $app->sendMail((
                        -MAIL_CONFIG_PARAMS => $params->{-MAIL_CONFIG_PARAMS},
                        -BODY               => $body,
                        -SUBJECT 	    => $subject,
                        @others_mail_send_params
                   ));
                   
                   
                }
            }

            if (!$addition_request_success) {
                $app->setNextViewToDisplay(
                    -VIEW_NAME => $params->{-ADD_FORM_VIEW_NAME}
                );
                $app->setAdditionalViewDisplayParam(
                    -PARAM_NAME => '-INPUT_WIDGET_CONFIG',
                    -PARAM_VALUE => $input_widget_definitions
                );

                $app->setAdditionalViewDisplayParam(
                    -PARAM_NAME => '-INPUT_WIDGET_DISPLAY_ORDER',
                    -PARAM_VALUE => $input_widget_display_order
                );
                return 1;
            }
            elsif ($params->{-DISPLAY_ACKNOWLEDGEMENT_ON_ADD_FLAG}) {
                $app->setNextViewToDisplay(
                    -VIEW_NAME => $params->{-ADD_ACKNOWLEDGEMENT_VIEW_NAME}
                );
                return 1;
            }

            else {
                return 2;
            }
        }

        else {
            die('You must specify a configuration for ' .
                '-BASIC_DATASOURCE_CONFIG_PARAMS in order to ' .
                'use loadData(). You may do so in the ' .
                '@ACTION_HANDLER_ACTION_PARAMS array ' .
               'in the application executable');
        }
    }

    return 0;
}

