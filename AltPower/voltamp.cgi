#!/usr/bin/perl -wT
<<<<<<< HEAD

# 	$Id: /AltPower/voltamp.cgi,v 0.81 2019/02/ 14:27:36 shanta Exp $	
# 	$Id: /AltPower/voltamp.cgi,v 0.8 2018/08/05 14:27:36 shanta Exp $	
my $version = '0.81';
=======
	

>>>>>>> CSC
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
<<<<<<< HEAD
# Foundation, Inc., 59 Temple Place - Suite 3 
# Boston, MA  02111-1307, USA.

use strict;

BEGIN{
    # Windows users must set a timezone env!
    $ENV{'TZ'} = 'EST' if ($^O =~ /MSWin32/i);
    use vars qw(@dirs);
    @dirs = qw(../Modules/
=======
# Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA  02111-1307, USA.
 
use strict;
BEGIN{
    use vars qw(@dirs);
    @dirs = qw(../Modules
>>>>>>> CSC
               ../Modules/CPAN .);
}
use lib @dirs;
unshift @INC, @dirs unless $INC[0] eq $dirs[0];

<<<<<<< HEAD
my @VIEWS_SEARCH_PATH = 
    qw(../Modules/Extropia/View/Todo
       ../Modules/Extropia/View/Default);

my @TEMPLATES_SEARCH_PATH = 
     qw(../HTMLTemplates/Apis
       ../HTMLTemplates/AltPower
       ../HTMLTemplates/BuyAndSell
       ../HTMLTemplates/ECF
       ../HTMLTemplates/CSPS 
       ../HTMLTemplates/CSC
       ../HTMLTemplates/ENCY 
       ../HTMLTemplates/HelpDesk
       ../HTMLTemplates/HE
       ../HTMLTemplates/IM
       ../HTMLTemplates/Organic
       ../HTMLTemplates/Shanta
       ../HTMLTemplates/Skye
       ../HTMLTemplates/Todo
       ../HTMLTemplates/TelMark
       ../HTMLTemplates/VitalVic
=======

my @VIEWS_SEARCH_PATH = 
    qw(../Modules/Extropia/View/Default);

my @TEMPLATES_SEARCH_PATH = 
    qw(../HTMLTemplates/Apis
       ../HTMLTemplates/AltPower
       ../HTMLTemplates/CSC
       ../HTMLTemplates/CSPS
       ../HTMLTemplates/ECF
       ../HTMLTemplates/ENCY
       ../HTMLTemplates/HelpDesk
       ../HTMLTemplates/Shanta
>>>>>>> CSC
       ../HTMLTemplates/Default);

use CGI qw(-debug);

#Carp commented out due to Perl 5.60 bug. Uncomment when using Perl 5.61.
#use CGI::Carp qw(fatalsToBrowser);

use Extropia::Core::App::DBApp;
use Extropia::Core::View;
use Extropia::Core::Action;
use Extropia::Core::SessionManager;

my $CGI = new CGI() or
    die("Unable to construct the CGI object" .
        ". Please contact the webmaster.");

<<<<<<< HEAD
foreach ($CGI->param()) {
    $CGI->param($1,$CGI->param($_)) if (/(.*)\.x$/);
}

######################################################################
#                          SITE SETUP                             #
######################################################################


my $APP_NAME = "CellLog";

my $APP_NAME_TITLE = "Cell Log";
my $SiteName =  $CGI->param('site') || "AltPower";
my $site_update;
=======

foreach ($CGI->param()) {
    $CGI->param($1,$CGI->param($_)) if (/(.*)\.x/);
}
######################################################################
#                          PORTING SETUP                             #
######################################################################
my $SiteName =  $CGI->param('site') || "AltPower";
my $APP_NAME = "VoltAmp";
my $APP_NAME_TITLE = $SiteName." Volt Amp Log";
>>>>>>> CSC
    my $homeviewname ;
    my $home_view; 
    my $BASIC_DATA_VIEW; 
    my $page_top_view;
    my $page_bottom_view;
<<<<<<< HEAD
    my $page_left_view;
=======
    my $left_page_view;
>>>>>>> CSC
#Mail settings
    my $mail_from; 
    my $mail_to;
    my $mail_replyto;
<<<<<<< HEAD
    my $CSS_VIEW_NAME = 'ApisCSSView';
=======
    my $CSS_VIEW_NAME = '/styles/CSCCSSView';
    my $CSS_VIEW_URL = $CSS_VIEW_NAME;
>>>>>>> CSC
    my $app_logo;
    my $app_logo_height;
    my $app_logo_width;
    my $app_logo_alt;
    my $IMAGE_ROOT_URL; 
    my $DOCUMENT_ROOT_URL;
    my $site;
    my $GLOBAL_DATAFILES_DIRECTORY;
    my $TEMPLATES_CACHE_DIRECTORY;
    my $APP_DATAFILES_DIRECTORY;
    my $DATAFILES_DIRECTORY;
    my $site_session;
    my $auth;
    my $MySQLPW;
    my $LINK_TARGET;
    my $HTTP_HEADER_PARAMS;
    my $HTTP_HEADER_KEYWORDS;
    my $HTTP_HEADER_DESCRIPTION;
    my $DBI_DSN;
    my $AUTH_TABLE;
    my  $AUTH_MSQL_USER_NAME;
<<<<<<< HEAD
    my $BuyDBI_DSN ='mysql:database=shanta_forager';
    my $BuyAUTH_MSQL_USER_NAME ='shanta_forager';
    my $BuyMySQLPW ='herbsrox2';
    my $DEFAULT_CHARSET; 
    my $additonalautusernamecomments;
    my $SetupVariables;
    my $TableName;
    my $sitename;
    my $ProjectTableName;
    my $mail_to_user;
    my $mail_to_member;
    my $mail_to_discussion;
    my $mail_list_bcc;
    my $SITE_DISPLAY_NAME = 'None Defined for this site.';
    my $last_update = 'Febuary 23, 2019';
    my $listname;
    my $AccountURL;
    my $subscrib;
    my $unsubscrib;
    my $listinfo;
    my $listfaq;
    my $SitedisplyName;
    my $salutaion;
    my $FAVICON;
    my $ANI_FAVICON;
    my $FAVICON_TYPE;
    my $CellCode = $CGI->param('CellCode');
    my $ModuleCode = $CGI->param('ModuleCode');
    my $BatteryCode = $CGI->param('Battery');
my $Affiliate = 001;


    my $HasMembers = 0;


use SiteSetup;
  my $UseModPerl = 1;
   $SetupVariables  = new SiteSetup($UseModPerl);
    $home_view             = $SetupVariables->{-HOME_VIEW}; 
    $homeviewname          = $SetupVariables->{-HOME_VIEW_NAME};
    $SITE_DISPLAY_NAME     = $SetupVariables->{-SITE_DISPLAY_NAME};
    $BASIC_DATA_VIEW       = $SetupVariables->{-BASIC_DATA_VIEW};
    $page_top_view         = $SetupVariables->{-PAGE_TOP_VIEW}||'PageTopView';
    $page_bottom_view      = $SetupVariables->{-PAGE_BOTTOM_VIEW};
    $page_left_view        = $SetupVariables->{-page_left_view};
    $MySQLPW               = $SetupVariables->{-MySQLPW};
    $DBI_DSN               = $SetupVariables->{-DBI_DSN};
    $HTTP_HEADER_PARAMS    = $SetupVariables->{-HTTP_HEADER_PARAMS};
    $HTTP_HEADER_KEYWORDS  = $SetupVariables->{-HTTP_HEADER_KEYWORDS};
    $HTTP_HEADER_DESCRIPTION = $SetupVariables->{-HTTP_HEADER_DESCRIPTION};
    $AUTH_TABLE            = $SetupVariables->{-AUTH_TABLE};
    $AUTH_MSQL_USER_NAME   = $SetupVariables->{-AUTH_MSQL_USER_NAME};
    $additonalautusernamecomments  = $SetupVariables->{-ADDITIONALAUTHUSERNAMECOMMENTS};
=======
    my $DEFAULT_CHARSET;
    my $additonalautusernamecomments;
    my $SetupVariables  ;
    my $CAL_TABLE;
    my $match_group_search = 0;
    my $match_use_mod = 0;
    my $match_user_search = 1;
    my $allow_mod ='1';
    my $allow_del = '1';
    my $auth_search = '0';
    my $require  = '0';
    my $reqire_user = '0';
    my $require_group = '0';
   my $HasMembers = 0;
   
use SiteSetup;
  my $UseModPerl = 0;
   $SetupVariables  = new SiteSetup($UseModPerl);
    $home_view             = $SetupVariables->{-HOME_VIEW}; 
    $homeviewname          = $SetupVariables->{-HOME_VIEW_NAME};
    $BASIC_DATA_VIEW       = $SetupVariables->{-BASIC_DATA_VIEW};
    $page_top_view         = $SetupVariables->{-PAGE_TOP_VIEW}||'PageTopView';
    $page_bottom_view      = $SetupVariables->{-PAGE_BOTTOM_VIEW};
    $left_page_view        = $SetupVariables->{-LEFT_PAGE_VIEW};
#MySQL settings
    $MySQLPW               = $SetupVariables->{-MySQLPW};
    $DBI_DSN               = $SetupVariables->{-DBI_DSN};
    $AUTH_TABLE            = $SetupVariables->{-AUTH_TABLE};
    $CAL_TABLE             = $SetupVariables->{-CAL_TABLE};
    $AUTH_MSQL_USER_NAME   = $SetupVariables->{-AUTH_MSQL_USER_NAME};
>>>>>>> CSC
#Mail settings
    $mail_from             = $SetupVariables->{-MAIL_FROM}; 
    $mail_to               = $SetupVariables->{-MAIL_TO};
    $mail_replyto          = $SetupVariables->{-MAIL_REPLYTO};
    $CSS_VIEW_NAME         = $SetupVariables->{-CSS_VIEW_NAME};
<<<<<<< HEAD
    my $CSS_VIEW_URL       = $SetupVariables->{-CSS_VIEW_NAME};
=======
    $CSS_VIEW_URL  = $SetupVariables->{-CSS_VIEW_NAME};
>>>>>>> CSC
    $app_logo              = $SetupVariables->{-APP_LOGO};
    $app_logo_height       = $SetupVariables->{-APP_LOGO_HEIGHT};
    $app_logo_width        = $SetupVariables->{-APP_LOGO_WIDTH};
    $app_logo_alt          = $SetupVariables->{-APP_LOGO_ALT};
    $IMAGE_ROOT_URL        = $SetupVariables->{-IMAGE_ROOT_URL}; 
    $DOCUMENT_ROOT_URL     = $SetupVariables->{-DOCUMENT_ROOT_URL};
    $LINK_TARGET           = $SetupVariables->{-LINK_TARGET};
    $HTTP_HEADER_PARAMS    = $SetupVariables->{-HTTP_HEADER_PARAMS};
<<<<<<< HEAD
    my $LocalIp            = $SetupVariables->{-LOCAL_IP};
    $Affiliate               = $SetupVariables->{-AFFILIATE};
    $site = $SetupVariables->{-DATASOURCE_TYPE};
    $GLOBAL_DATAFILES_DIRECTORY = $SetupVariables->{-GLOBAL_DATAFILES_DIRECTORY}||'/home/shanta/';
    $TEMPLATES_CACHE_DIRECTORY  = $GLOBAL_DATAFILES_DIRECTORY.$SetupVariables->{-TEMPLATES_CACHE_DIRECTORY,};
    $APP_DATAFILES_DIRECTORY    = $SetupVariables->{-APP_DATAFILES_DIRECTORY};
    $DATAFILES_DIRECTORY   = $APP_DATAFILES_DIRECTORY;
    $site_session          = $GLOBAL_DATAFILES_DIRECTORY.'/Sessions';
    $auth                  = $DATAFILES_DIRECTORY.'/csc.admin.users.dat';
    $TableName             = 'voltamp_tb';
    $ProjectTableName      = 'csc_project_tb';
	 my $DropListName       = 'buy_sell_category_tb';
 
#Add sub aplication spacific overrides.
# $GLOBAL_DATAFILES_DIRECTORY = "Datafiles";
# $TEMPLATES_CACHE_DIRECTORY  = "$GLOBAL_DATAFILES_DIRECTORY/TemplatesCache";
# $APP_DATAFILES_DIRECTORY    = "Datafiles/Todo";
$page_top_view    = $CGI->param('page_top_view')||$page_top_view;
$page_bottom_view = $CGI->param('page_bottom_view')||$page_bottom_view;
#$page_left_view   = $CGI->param('page_left_view')||$page_left_view;
$page_left_view = "LeftPageView";
my $target;
my $columnstoview;
my $SortFields;
my $SortField1;
my $SortField2;
my $SortDirection;
my $RecordsToDisplay;



if ($CGI->param('page_top_view') eq'SBPageTopView'){
$target='_content';
 $columnstoview = [qw(
        category
        CellCode
        sart_date
       )];
 $SortFields=[qw(
        CellCode
        start_date
        )];
 $SortField2='start_day';
 $SortField1='CellCode';
 $SortDirection='DESC' ;
 $RecordsToDisplay=20;
}else{
$target='_self';
 $columnstoview=[qw(
        category
        item_name
        price
        url
        location

        )];
$SortFields=[qw(
        category
        location
        )];
 $SortField1=$CGI->param('sort_field1') ||'CellCode';
 $SortField2=$CGI->param('sort_field2') ||'start_day';
 $RecordsToDisplay=100;
 $SortDirection='DESC';#ASC
}
my $SESSION_DIR;
$LINK_TARGET = $target;
=======
    $HTTP_HEADER_KEYWORDS     = $SetupVariables->{-HTTP_HEADER_KEYWORDS};
    $HTTP_HEADER_DESCRIPTION  = $SetupVariables->{-HTTP_HEADER_DESCRIPTION};
    $site = $SetupVariables->{-DATASOURCE_TYPE};
    $GLOBAL_DATAFILES_DIRECTORY = $SetupVariables->{-GLOBAL_DATAFILES_DIRECTORY}||'BLANK';
    $TEMPLATES_CACHE_DIRECTORY  = $GLOBAL_DATAFILES_DIRECTORY.$SetupVariables->{-TEMPLATES_CACHE_DIRECTORY,};
    $APP_DATAFILES_DIRECTORY    = $SetupVariables->{-APP_DATAFILES_DIRECTORY};
    $DATAFILES_DIRECTORY = $APP_DATAFILES_DIRECTORY;
    $site_session = $DATAFILES_DIRECTORY.'/Sessions';
    $auth = $DATAFILES_DIRECTORY.'/csc.admin.users.dat';


>>>>>>> CSC
my $VIEW_LOADER = new Extropia::Core::View
    (\@VIEWS_SEARCH_PATH,\@TEMPLATES_SEARCH_PATH) or
    die("Unable to construct the VIEW LOADER object in " . $CGI->script_name() .
        " Please contact the webmaster.");

<<<<<<< HEAD
use constant HAS_CLASS_DATE  => eval { require Class::Date; };

=======
>>>>>>> CSC
######################################################################
#                          SESSION SETUP                             #
######################################################################

my @SESSION_CONFIG_PARAMS = (
    -TYPE            => 'File',
<<<<<<< HEAD
    -MAX_MODIFY_TIME => 60 * 60 * 2,
    -SESSION_DIR     => "$GLOBAL_DATAFILES_DIRECTORY/Sessions",
    -FATAL_TIMEOUT   => 0,
    -FATAL_SESSION_NOT_FOUND => 1
=======
    -MAX_MODIFY_TIME => 60 * 60,
    -SESSION_DIR     => "$GLOBAL_DATAFILES_DIRECTORY/Sessions",
    -FATAL_TIMEOUT   => 0,
    -FATAL_SESSION_NOT_FOUND => 0
>>>>>>> CSC
);

######################################################################
#                     SESSION MANAGER SETUP                          #
######################################################################
<<<<<<< HEAD

=======
>>>>>>> CSC
my @SESSION_MANAGER_CONFIG_PARAMS = (
    -TYPE           => 'FormVar',
    -CGI_OBJECT     => $CGI,
    -SESSION_PARAMS => \@SESSION_CONFIG_PARAMS
);

my $SESSION_MGR = Extropia::Core::SessionManager->create(
    @SESSION_MANAGER_CONFIG_PARAMS
);

my $SESSION    = $SESSION_MGR->createSession();
my $SESSION_ID = $SESSION->getId();
<<<<<<< HEAD

#Deal with site setup in session files. This code need taint checking.
=======
#my $CSS_VIEW_URL = $CGI->script_name(). "?display_css_view=on&session_id=$SESSION_ID";

>>>>>>> CSC
if ($CGI->param('site')){
    if  ($CGI->param('site') ne $SESSION ->getAttribute(-KEY => 'SiteName') ){
      $SESSION ->setAttribute(-KEY => 'SiteName', -VALUE => $CGI->param('site')) ;
       $SiteName = $CGI->param('site');
    }else {
	$SESSION ->setAttribute(-KEY => 'SiteName', -VALUE => $SiteName );
    }
	 
}else {
  if ( $SESSION ->getAttribute(-KEY => 'SiteName')) {
    $SiteName = $SESSION ->getAttribute(-KEY => 'SiteName');
  }else {
	$SESSION ->setAttribute(-KEY => 'SiteName', -VALUE => $SiteName );
      }
}
<<<<<<< HEAD
my $username = $SESSION ->getAttribute(-KEY => 'auth_username');
$sitename =$SiteName;
my $GROUP_OF_POSTER = $SESSION -> getAttribute(-KEY => 'auth_groups')||'normal';
my $group    =  $SESSION ->getAttribute(-KEY => 'auth_group');

my $apsubmenu = 'BuyApplicationSubMenuView';
if  ($CGI->param('view') eq 'ContactView'){
 $apsubmenu ='' ;
}
my $footer           = " ----------------------------------------
You received this email because you requested a subscription to ."
.$listname
." We apologise if you received it in error or if your information is incorrect.
Please follow the instructions below to unsubcribe or change your settings:

Point your browser at  " .$AccountURL." to manage your account.

Alternatively, use the email commands:

Subscribe To " .$listname."
Send email to " .$subscrib."
 Unsubscribe From " .$listname." : Send email to
  " .$unsubscrib ."


Send mail to the following for info and FAQ for this list:
".$listinfo ." ". $listfaq ."

The ".$SitedisplyName ." respects your privacy. We do not sell our mailing list information nor do we release your information to anyone, except as required by law.

Thanks,"
.$salutaion;
    $auth = $DATAFILES_DIRECTORY.'/csc.admin.users.dat';
if ($CGI->param('embed')){
   $page_top_view = "EmbedPageTopView";
   $page_bottom_view = "";
   $RecordsToDisplay = 10;
   }

=======


if ($CGI->param('embed')){
   $page_top_view = "EmbedPageTopView";
   $page_bottom_view = "";
   $allow_mod ='0';
   $allow_del = '0';
   $auth_search = '0';
   $require  = '0';
 }
>>>>>>> CSC

######################################################################
#                       AUTHENTICATION SETUP                         #
######################################################################

my @AUTH_USER_DATASOURCE_FIELD_NAMES = qw(
    username
    password
    groups
    firstname
    lastname
    email
);

<<<<<<< HEAD
#CSC comversion to auth swiching from SiteSetup.pm At momet this is only set to switch from  
# file to MySQL

=======
>>>>>>> CSC
my @AUTH_USER_DATASOURCE_PARAMS;
if ($site eq "file") {

	@AUTH_USER_DATASOURCE_PARAMS = (
	    -TYPE                       => 'File',
	    -FIELD_DELIMITER            => '|',
	    -CREATE_FILE_IF_NONE_EXISTS => 1,
	    -FIELD_NAMES                => \@AUTH_USER_DATASOURCE_FIELD_NAMES,
	    -FILE                       => "$APP_DATAFILES_DIRECTORY/$APP_NAME.users.dat"
	);
}
else {

   @AUTH_USER_DATASOURCE_PARAMS = (
        -TYPE         => 'DBI',
<<<<<<< HEAD
        -DBI_DSN      => $DBI_DSN,
=======
        -DBI_DSN      =>  $DBI_DSN,
>>>>>>> CSC
        -TABLE        => $AUTH_TABLE,
        -USERNAME     => $AUTH_MSQL_USER_NAME,
        -PASSWORD     => $MySQLPW,
        -FIELD_NAMES  => \@AUTH_USER_DATASOURCE_FIELD_NAMES
    );
}

<<<<<<< HEAD
=======


>>>>>>> CSC
my @AUTH_ENCRYPT_PARAMS = (
    -TYPE => 'Crypt'
);

my %USER_FIELDS_TO_DATASOURCE_MAPPING = (
    'auth_username'  => 'username',
    'auth_password'  => 'password',
    'auth_firstname' => 'firstname',
    'auth_lastname'  => 'lastname',
    'auth_groups'    => 'groups',
    'auth_email'     => 'email'
);

my @AUTH_CACHE_PARAMS = (
    -TYPE           => 'Session',
    -SESSION_OBJECT => $SESSION
);

my @AUTH_CONFIG_PARAMS = (
    -TYPE                                => 'DataSource',
    -USER_DATASOURCE_PARAMS              => \@AUTH_USER_DATASOURCE_PARAMS,
    -ENCRYPT_PARAMS                      => \@AUTH_ENCRYPT_PARAMS,
    -ADD_REGISTRATION_TO_USER_DATASOURCE => 1,
    -USER_FIELDS_TO_DATASOURCE_MAPPING   => \%USER_FIELDS_TO_DATASOURCE_MAPPING,
    -AUTH_CACHE_PARAMS                   => \@AUTH_CACHE_PARAMS
);

######################################################################
#                 AUTHENTICATION MANAGER SETUP                       #
######################################################################

my @AUTH_VIEW_DISPLAY_PARAMS = (
    -SITE_NAME            => $SiteName,
    -CSS_VIEW_URL            => $CSS_VIEW_URL,
    -APPLICATION_LOGO        => $app_logo,
    -APPLICATION_LOGO_HEIGHT => $app_logo_height,
    -APPLICATION_LOGO_WIDTH  => $app_logo_width,
<<<<<<< HEAD
    -APPLICATION_LOGO_ALT    => $APP_NAME_TITLE,
    -DOCUMENT_ROOT_URL       => $DOCUMENT_ROOT_URL,
    -HTTP_HEADER_PARAMS      => $HTTP_HEADER_PARAMS,
    -LINK_TARGET             => $LINK_TARGET,
    -IMAGE_ROOT_URL          => $IMAGE_ROOT_URL,
    -SCRIPT_DISPLAY_NAME     => $APP_NAME_TITLE,
    -SCRIPT_NAME             => $CGI->script_name(),
    -PAGE_TOP_VIEW           => $page_top_view,
    -PAGE_BOTTOM_VIEW        => $page_bottom_view,
    -page_left_view          => $page_left_view,
    -LINK_TARGET             => $LINK_TARGET,
    -DEFAULT_CHARSET         => $DEFAULT_CHARSET,
=======
    -APPLICATION_LOGO_ALT    => $app_logo_alt,
    -DOCUMENT_ROOT_URL       => $DOCUMENT_ROOT_URL,
    -HTTP_HEADER_PARAMS      => $HTTP_HEADER_PARAMS,
    -IMAGE_ROOT_URL          => $IMAGE_ROOT_URL,
    -SCRIPT_DISPLAY_NAME     => $APP_NAME_TITLE,
    -SCRIPT_NAME             => $CGI->script_name(),
    -PAGE_TOP_VIEW                          => $CGI->param('page_top_view')||$page_top_view,
    -PAGE_BOTTOM_VIEW                       => $CGI->param('page_bottom_view')||$page_bottom_view,
    -LEFT_PAGE_VIEW                         => $CGI->param('left_page_view')||$left_page_view,
    -LINK_TARGET             => $LINK_TARGET
>>>>>>> CSC
);

my @AUTH_REGISTRATION_DH_MANAGER_PARAMS = (
    -TYPE         => 'CGI',
    -CGI_OBJECT   => $CGI,
    -DATAHANDLERS => [qw(
        Email
        Exists
    )],
    
    -FIELD_MAPPINGS => {
                'auth_username'     => 'Username',
                'auth_password'     => 'Password',
                'auth_password2'    => 'Confirm Password',
                'auth_firstname'    => 'First Name',
                'auth_lastname'     => 'Last Name',
                'auth_email'        => 'E-Mail Address'
        },
  
        -IS_FILLED_IN => [qw(
                auth_username
                auth_firstname
                auth_lastname
                auth_email
        )],
    
        -IS_EMAIL => [qw(
                auth_email
        )]
);
    
<<<<<<< HEAD
my @USER_FIELDS = (qw(
=======
my @USER_FIELDS = qw(
>>>>>>> CSC
    auth_username
    auth_password
    auth_groups
    auth_firstname
    auth_lastname
    auth_email
<<<<<<< HEAD
));
=======
);
>>>>>>> CSC

my %USER_FIELD_NAME_MAPPINGS = (
    'auth_username'  => 'Username',
    'auth_password'  => 'Password',
    'auth_groups'    => 'Groups',
    'auth_firstname' => 'First Name',
    'auth_lastname'  => 'Last Name',
    'auth_email'     => 'E-Mail'
);

my %USER_FIELD_TYPES = (
    -USERNAME_FIELD => 'auth_username',
    -PASSWORD_FIELD => 'auth_password',
    -GROUP_FIELD    => 'auth_groups',
    -EMAIL_FIELD    => 'auth_email'
);

my @MAIL_PARAMS = (
    -TYPE         => 'Sendmail',
);

my @USER_MAIL_SEND_PARAMS = (
<<<<<<< HEAD
    -FROM    => $SESSION ->getAttribute(-KEY => 'auth_email')||$mail_from,
    -TO      => $SetupVariables->{-MAIL_TO_ADMIN}||$mail_to,
    -SUBJECT => $APP_NAME_TITLE.' Password Generated'
);
 
my @ADMIN_MAIL_SEND_PARAMS = (
    -FROM    => $SESSION ->getAttribute(-KEY => 'auth_email')||$mail_from,
    -TO      => $SetupVariables->{-MAIL_TO_ADMIN}||$mail_to,
    -SUBJECT => $APP_NAME_TITLE.' Registration Notification'
);
                
=======
    -FROM    => $mail_from,
    -TO      => $mail_to,
    -SUBJECT => $APP_NAME_TITLE.' Password Generated'
);

my @ADMIN_MAIL_SEND_PARAMS = (
    -FROM    => $mail_from,
    -TO      => $mail_to,
    -SUBJECT => $APP_NAME_TITLE.' Registration Notification'
);

>>>>>>> CSC
my @AUTH_MANAGER_CONFIG_PARAMS = (
    -TYPE                        => 'CGI',
    -ADMIN_MAIL_SEND_PARAMS      => \@ADMIN_MAIL_SEND_PARAMS,
    -AUTH_VIEW_PARAMS            => \@AUTH_VIEW_DISPLAY_PARAMS,
    -MAIL_PARAMS                 => \@MAIL_PARAMS,
    -USER_MAIL_SEND_PARAMS       => \@USER_MAIL_SEND_PARAMS,
    -SESSION_OBJECT              => $SESSION,
    -LOGON_VIEW                  => 'AuthManager/CGI/LogonScreen',
    -REGISTRATION_VIEW           => 'AuthManager/CGI/RegistrationScreen',
    -REGISTRATION_SUCCESS_VIEW   => 'AuthManager/CGI/RegistrationSuccessScreen',
    -SEARCH_VIEW                 => 'AuthManager/CGI/SearchScreen',
    -SEARCH_RESULTS_VIEW         => 'AuthManager/CGI/SearchResultsScreen',
    -VIEW_LOADER                 => $VIEW_LOADER,
    -AUTH_PARAMS                 => \@AUTH_CONFIG_PARAMS,
    -CGI_OBJECT                  => $CGI,
<<<<<<< HEAD
    -ALLOW_REGISTRATION          => 1,   
=======
    -ALLOW_REGISTRATION          => 0,   
>>>>>>> CSC
    -ALLOW_USER_SEARCH           => 0,
    -USER_SEARCH_FIELD           => 'auth_email',
    -GENERATE_PASSWORD           => 0,
    -DEFAULT_GROUPS              => 'normal',
<<<<<<< HEAD
    -EMAIL_REGISTRATION_TO_ADMIN => 1,
=======
    -EMAIL_REGISTRATION_TO_ADMIN => 0,
>>>>>>> CSC
    -USER_FIELDS                 => \@USER_FIELDS,
    -USER_FIELD_TYPES            => \%USER_FIELD_TYPES,
    -USER_FIELD_NAME_MAPPINGS    => \%USER_FIELD_NAME_MAPPINGS,
    -DISPLAY_REGISTRATION_AGAIN_AFTER_FAILURE => 1,
    -AUTH_REGISTRATION_DH_MANAGER_PARAMS => \@AUTH_REGISTRATION_DH_MANAGER_PARAMS
);

######################################################################
#                      DATA HANDLER SETUP                            #
######################################################################
<<<<<<< HEAD

my @ADD_FORM_DHM_CONFIG_PARAMS = (
    -TYPE         => 'CGI',
    -CGI_OBJECT   => $CGI,
    -DATAHANDLERS => [qw(
        Email
=======
                       
my @ADD_FORM_DHM_CONFIG_PARAMS = (
    -TYPE         => 'CGI',
    -CGI_OBJECT   => $CGI,  
    -DATAHANDLERS => [qw(
        Email 
>>>>>>> CSC
        Exists
        HTML
        String
        )],

<<<<<<< HEAD
    -FIELD_MAPPINGS =>
      {
       CellCode         => 'CellCode',
       start_date       => 'Start Date',
       due_date         => 'Due Date',
       subject          => 'Subject',
       estimated_man_hours 	=> 'Estimated Man Hours',
       accumulative_time 	=> 'Accumulated time',
       category	      	=> 'Project Code',
       Volts            => 'Voltage',
       status           => 'Status',
       Temp             => 'Tempurature',
       last_mod_by      => 'Last Modified By',
       last_mod_date    => 'Last Modified Date',
      },

    -RULES => [
      #  -ESCAPE_HTML_TAGS => [
      #      -FIELDS => [qw(
      #          *
      #      )]
      #  ],
=======
    -FIELD_MAPPINGS => {
        'Volt'           => 'Voltage',
        sitename	      	=> 'SiteName',
        'time'           => 'Time',
        'Amp'            => 'Amperage',
        'comments'       => 'Comments'
    },

    -RULES => [
        -ESCAPE_HTML_TAGS => [
            -FIELDS => [qw(
                *
            )],
        ],
>>>>>>> CSC

        -DOES_NOT_CONTAIN => [
            -FIELDS => [qw(
                *
            )],

            -CONTENT_TO_DISALLOW => '\\',
            -ERROR_MESSAGE => "You may not have a '\\' character in the " .
                              "%FIELD_NAME% field."
        ],

        -DOES_NOT_CONTAIN => [
            -FIELDS => [qw(
                *
            )],

            -CONTENT_TO_DISALLOW => '\"',
            -ERROR_MESSAGE => "You may not have a '\"' character in the " .
                              "%FIELD_NAME% field."
        ],

<<<<<<< HEAD

        -IS_EMAIL => [
            -FIELDS => [qw(
            email
            )],

            -ERROR_MESSAGE => '%FIELD_VALUE% is not a valid value ' .
                              'for %FIELD_NAME%.'
        ],

=======
>>>>>>> CSC
        -SUBSTITUTE_ONE_STRING_FOR_ANOTHER => [
            -FIELDS => [qw(
                *
            )],
            -ORIGINAL_STRING => '"',
            -NEW_STRING => "''"
        ],

        -IS_FILLED_IN => [
<<<<<<< HEAD
            -FIELDS => [
                        qw(
                          )
                       ]
=======
            -FIELDS => [qw(
             )]
>>>>>>> CSC
        ]
    ]
);

my @MODIFY_FORM_DHM_CONFIG_PARAMS = (
    -TYPE         => 'CGI',
    -CGI_OBJECT   => $CGI,  
    -DATAHANDLERS => [qw(
        Email 
        Exists
        HTML
        String
        )],

    -FIELD_MAPPINGS => {
<<<<<<< HEAD
       start_date       => 'Start Date',
       due_date         => 'Due Date',
       subject          => 'Subject',
       description      => 'Description',
       Volts	      	=> 'Voltage',
       estimated_man_hours 	=> 'Estimated Man Hours',
       accumulative_time 	=> 'Accumulated time',
       status           => 'Status',
       Temp             => 'Tempurature',
    },

    -RULES => [
      #  -ESCAPE_HTML_TAGS => [
      #      -FIELDS => [qw(
      #          *
      #      )]
      #  ],
=======
         'Volt'           => 'Voltage',
         sitename	      	=> 'SiteName',
         'time'           => 'Time',
         'Amp'            => 'Amperage',
         'comments'       => 'Comments'
     },

    -RULES => [
        -ESCAPE_HTML_TAGS => [
            -FIELDS => [qw(
                *
            )],
        ],
>>>>>>> CSC

        -DOES_NOT_CONTAIN => [
            -FIELDS => [qw(
                *
            )],

            -CONTENT_TO_DISALLOW => '\\',
            -ERROR_MESSAGE => "You may not have a '\\' character in the " .
                              "%FIELD_NAME% field."
        ],

        -DOES_NOT_CONTAIN => [
            -FIELDS => [qw(
                *
            )],

            -CONTENT_TO_DISALLOW => '\"',
            -ERROR_MESSAGE => "You may not have a '\"' character in the " .
                              "%FIELD_NAME% field."
        ],

<<<<<<< HEAD
        -IS_EMAIL => [
            -FIELDS => [qw(
                email
            )],

            -ERROR_MESSAGE => '%FIELD_VALUE% is not a valid value ' .
                              'for %FIELD_NAME%.'
        ],

=======
>>>>>>> CSC
        -SUBSTITUTE_ONE_STRING_FOR_ANOTHER => [
            -FIELDS => [qw(
                *
            )],
            -ORIGINAL_STRING => '"',
            -NEW_STRING => "''"
        ],

<<<<<<< HEAD
        -IS_FILLED_IN => [
            -FIELDS => [qw(
                           )
                       ]
=======
            -IS_FILLED_IN => [
            -FIELDS => [qw(
            )]
>>>>>>> CSC
        ]
    ]
);

my @DATA_HANDLER_MANAGER_CONFIG_PARAMS = (
    -ADD_FORM_DHM_CONFIG_PARAMS    => \@ADD_FORM_DHM_CONFIG_PARAMS,
    -MODIFY_FORM_DHM_CONFIG_PARAMS => \@MODIFY_FORM_DHM_CONFIG_PARAMS,
);

######################################################################
#                      DATASOURCE SETUP                              #
######################################################################

<<<<<<< HEAD
my @DATASOURCE_FIELD_NAMES = 
    qw(
       record_id
       sitename
       start_day 	
       time 	
       BatteryCode 
       ModuleCode	
       CellCode 	
       Volts 	
       Amps 	
       Temp 	
       location
       comments 	
       description
       time
       status
       share
       last_mod_by
       last_mod_date
       username_of_poster
       group_of_poster
       date_time_posted 
      );

# prepare the data then used in the form input definition
my @months = qw(January February March April May June July August
                September October November December);
my %months;
@months{1..@months} = @months;
my %years = ();
$years{$_} = $_ for (2017..2025);
my %days  = ();
$days{$_} = $_ for (1..31);

my %priority =
    (
      1 => 'LOW',
      2 => 'MIDDLE',
      3 => 'HIGH',
    );

my %status =
    (
      1 => 'NEW',
      2 => 'On hand',
      3 => 'Sold',
    );

my %BatteryCode =
 (
      'Main24volt' => 'Main 24 Volt Pack',
      '12v'  => '12 Volt lead Acid 2 6',
    );
    
 my %ModuleCode =
 (
      241  => 'Module 1',
      242  => 'Module 2',
      243  => 'Module 3',  
      244  => '4',
      245  => '5',
      246  => '5',
      247  => '5',
       );
    
my %CellCode =
 (
      1    => '7s 18650 1',  
      2    => '7s 18650 2',
      3    => '7s 18650 3',
      4    => '7s 18650 4',
      5    => '7s 18650 5',
      6    => '7s 18650 6',
      7    => '7s 18650 7',
    );
my %BASIC_INPUT_WIDGET_DEFINITIONS = 
    (
     BatteryCode => [
                 -DISPLAY_NAME => 'BatteryCode',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'BatteryCode',
                 -SIZE         => 44,
                 -VALUES       => [sort {$a <=> $b} keys %BatteryCode],
 		         -LABELS       => \%BatteryCode,
               ],

   ModuleCode => [
                 -DISPLAY_NAME => 'ModuleCode',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'ModuleCode',
                 -SIZE         => 44,
                 -VALUES       => [sort {$a <=> $b} keys %ModuleCode],
 		         -LABELS       => \%ModuleCode,
               ],
   CellCode => [
                 -DISPLAY_NAME => 'CellCode',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'CellCode',
                 -SIZE         => 44,
                 -VALUES       => [sort {$a <=> $b} keys %CellCode],
 		         -LABELS       => \%CellCode,
               ],
 description  => [
                 -DISPLAY_NAME => 'Description',
                 -TYPE         => 'textarea',
                 -NAME         => 'description',
                 -ROWS         => 8,
                 -COLS         => 42,
                 -WRAP         => 'VIRTUAL',
                 -INPUT_CELL_COLSPAN => 3,
               ],

     start_day => [
                 -DISPLAY_NAME => 'Date add to start',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'start_day',
                 -VALUES       => [1..31],
                ],

     start_mon => [
                 -DISPLAY_NAME => '',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'start_mon',
                 -VALUES       => [1..12],
                 -LABELS       => \%months,
                ],

     start_year => [
                 -DISPLAY_NAME => '',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'start_year',
                 -VALUES       => [sort {$a <=> $b} keys %years],
                ],

     due_day => [
                 -DISPLAY_NAME => 'Due Date',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'due_day',
                 -VALUES       => [1..31],
                ],

     due_mon => [
                 -DISPLAY_NAME => '',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'due_mon',
                 -VALUES       => [1..12],
                 -LABELS       => \%months,
                ],

     due_year => [
                 -DISPLAY_NAME => '',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'due_year',
                 -VALUES       => [sort {$a <=> $b} keys %years],
                ],

  share => [
        -DISPLAY_NAME => 'What level of sharing do you want? ',
        -TYPE         => 'popup_menu',
        -NAME         => 'share',
        -LABELS  => { 
               '' 	=> "I'm not sure",
               'pub'		=> 'All sites.',
               'priv'		=> 'Only This Site.',
        },
        -VALUES       => [
                      '',
                      'pub',
                      'priv',
        ]
    ],

     priority => [
                 -DISPLAY_NAME => 'Priority',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'priority',
                 -VALUES       => [sort {$a cmp $b} keys %priority],
                 -LABELS       => \%priority,
                 -INPUT_CELL_COLSPAN => 3,
                ],

     status => [
                 -DISPLAY_NAME => 'Status',
                 -TYPE         => 'popup_menu',
                 -NAME         => 'status',
                 -VALUES       => [sort {$a cmp $b} keys %status],
		 -LABELS       => \%status,
                 -INPUT_CELL_COLSPAN => 3,
                ],
   #   CellCode  => [
   #     -DISPLAY_NAME => 'CellCode',
   #     -TYPE         => 'textfield',
   #     -NAME         => 'CellCode',
   #     -SIZE         => 30,
	#    -VALUE        => $CellCode,
   #     -MAXLENGTH    => 80
   # ],

     sitename => [
        -DISPLAY_NAME => 'Site Name',
        -TYPE         => 'textfield',
        -NAME         => 'sitename',
        -SIZE         => 30,
	    -VALUE        => $SiteName,
        -MAXLENGTH    => 80
    ],

     price => [
        -DISPLAY_NAME => 'Item price',
        -TYPE         => 'textfield',
        -NAME         => 'price',
=======
my @DATASOURCE_FIELD_NAMES = qw(
        record_id
        sitename
        time
        Volts
        Amps
        BatteryCode
        CellCode
        comments        
        username_of_poster
        group_of_poster
        date_time_posted
);

my %BASIC_INPUT_WIDGET_DEFINITIONS = (
 
    sitename => [
        -DISPLAY_NAME => 'Site name code',
        -TYPE         => 'textfield',
        -NAME         => 'sitename',
        -VALUE        => $SiteName,
        -SIZE         => 30,
        -MAXLENGTH    => 80
    ],

   Volts => [
        -DISPLAY_NAME => 'Voltage',
        -TYPE         => 'textfield',
        -NAME         => 'Volts',
>>>>>>> CSC
        -SIZE         => 30,
        -MAXLENGTH    => 80
    ],

<<<<<<< HEAD
     time => [
        -DISPLAY_NAME => "Time stamp 0000-00-00 00:00:00",
        -TYPE         => 'textfield',
        -NAME         => 'time',
        -SIZE         => 80,
        -MAXLENGTH    => 150
    ],
    
     email => [
        -DISPLAY_NAME => 'Email address',
        -TYPE         => 'textfield',
        -NAME         => 'email',
        -SIZE         => 30,
        -MAXLENGTH    => 75
    ],
 
     Temp => [
        -DISPLAY_NAME => 'Tempurture in Celcus',
        -TYPE         => 'textfield',
        -NAME         => 'Temp',
        -VALUE        => '1',
        -SIZE         => 3,
        -MAXLENGTH    => 80
    ],
     Amps => [
=======
   BatteryCode => [
        -DISPLAY_NAME => 'Battery Code',
        -TYPE         => 'textfield',
        -NAME         => 'BatteryCode',
        -SIZE         => 30,
        -MAXLENGTH    => 80
    ],
  CellCode => [
        -DISPLAY_NAME => 'Cell Code',
        -TYPE         => 'textfield',
        -NAME         => 'CellCode',
        -SIZE         => 30,
        -MAXLENGTH    => 80
    ],
   Amps => [
>>>>>>> CSC
        -DISPLAY_NAME => 'Amperage',
        -TYPE         => 'textfield',
        -NAME         => 'Amps',
        -SIZE         => 30,
        -MAXLENGTH    => 80
    ],
<<<<<<< HEAD
     Volts => [
        -DISPLAY_NAME => 'Volts',
        -TYPE         => 'textfield',
        -NAME         => 'Volts',
        -SIZE         => 30,
        -MAXLENGTH    => 250
    ],

    location => [
        -DISPLAY_NAME => 'Location of item.',
        -TYPE         => 'textfield',
        -NAME         => 'location',
        -SIZE         => 30,
        -MAXLENGTH    => 100
    ],

=======
    time => [
        -DISPLAY_NAME => 'time',
        -TYPE         => 'textfield',
        -NAME         => 'time',
        -SIZE         => 30,
        -MAXLENGTH    => 80
    ],
>>>>>>> CSC
    comments => [
        -DISPLAY_NAME => 'Comments',
        -TYPE         => 'textarea',
        -NAME         => 'comments',
        -ROWS         => 6,
        -COLS         => 30,
        -WRAP         => 'VIRTUAL'
<<<<<<< HEAD
    ],
   );
#      [qw(due_day due_mon due_year)]


my @BASIC_INPUT_WIDGET_DISPLAY_ORDER =  (
     qw(sitename), 
     qw(BatteryCode),
     qw(ModuleCode),
     qw(CellCode),
     [qw(start_day start_mon start_year)],
     qw(Volts),
     qw(Amps),
     qw(Temp),
     qw(time),
     [qw(location)],
     qw(description),
     qw(comments),
     [qw(status)],
     qw(share),
    );


my %ACTION_HANDLER_PLUGINS =
    (

 #    'Default::DisplayAddFormAction' =>
 #    {
 #     -DisplayAddFormAction     => [qw(Plugin::Todo::DisplayAddFormAction)],
 #    },

     'Default::DisplayDetailsRecordViewAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

     'Default::DisplayDeleteRecordConfirmationAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

     'Default::DisplayModifyFormAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

     'Default::DisplayModifyRecordConfirmationAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

     'Default::ProcessModifyRequestAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

     'Default::DisplayAddRecordConfirmationAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

     'Default::ProcessAddRequestAction' => 
     {
      -loadData_END             => [qw(Plugin::Todo::DBRecords2InputFields)],
      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
     },

 #    'Default::DefaultAction' => 
 #    {
 #     -loadData_END             => [qw(Plugin::Todo::Records2Display)],
 #     -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
 #    },

 #    'Default::DisplayViewAllRecordsAction' => 
 #    {
 #     -loadData_END             => [qw(Plugin::Todo::Records2Display)],
 #     -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
 #    },

 #    'Default::DisplaySimpleSearchResultsAction' => 
#     {
#      -loadData_END             => [qw(Plugin::Todo::Records2Display)],
#      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
#     },

#     'Default::DisplayOptionsFormAction' => 
#     {
#      -loadData_END             => [qw(Plugin::Todo::Records2Display)],
#      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
#     },

#     'Default::DisplayPowerSearchFormAction' => 
#     {
#      -loadData_END             => [qw(Plugin::Todo::Records2Display)],
#      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
#     },

#     'Default::PerformPowerSearchAction' => 
#     {
#      -loadData_END             => [qw(Plugin::Todo::Records2Display)],
#      -handleIncomingData_BEGIN => [qw(Plugin::Todo::InputFields2DBFields)],
#     },



    );

=======
    ]
);

my @BASIC_INPUT_WIDGET_DISPLAY_ORDER = qw(
        sitename
        time
        Volts
        Amps
        BatteryCode
        CellCode
        comments 
);
>>>>>>> CSC

my @INPUT_WIDGET_DEFINITIONS = (
    -BASIC_INPUT_WIDGET_DEFINITIONS => \%BASIC_INPUT_WIDGET_DEFINITIONS,
    -BASIC_INPUT_WIDGET_DISPLAY_ORDER => \@BASIC_INPUT_WIDGET_DISPLAY_ORDER
);
<<<<<<< HEAD
#$site = 'file';
my @BASIC_DATASOURCE_CONFIG_PARAMS;
if ($site eq "file"){
 @BASIC_DATASOURCE_CONFIG_PARAMS = (    -TYPE                       => 'File',
    -FILE                       => "$APP_DATAFILES_DIRECTORY/$TableName.dat",
=======
my @BASIC_DATASOURCE_CONFIG_PARAMS;
if ($site eq "file"){
 @BASIC_DATASOURCE_CONFIG_PARAMS = (    -TYPE                       => 'File', 
    -FILE                       => "$APP_DATAFILES_DIRECTORY/$APP_NAME.dat",
>>>>>>> CSC
    -FIELD_DELIMITER            => '|',
    -COMMENT_PREFIX             => '#',
    -CREATE_FILE_IF_NONE_EXISTS => 1,
    -FIELD_NAMES                => \@DATASOURCE_FIELD_NAMES,
    -KEY_FIELDS                 => ['record_id'],
    -FIELD_TYPES                => {
                                    record_id        => 'Autoincrement',
                                    datetime         => 
                                    [
                                     -TYPE  => "Date",
                                     -STORAGE => 'y-m-d H:M:S',
                                     -DISPLAY => 'y-m-d H:M:S',
                                    ],
                                   },
);
}
else{
	@BASIC_DATASOURCE_CONFIG_PARAMS = (
	        -TYPE         => 'DBI',
	        -DBI_DSN      => $DBI_DSN,
<<<<<<< HEAD
	        -TABLE        => $TableName,
	        -USERNAME     => $AUTH_MSQL_USER_NAME,
	        -PASSWORD     => $MySQLPW,
	        -FIELD_NAMES  => \@DATASOURCE_FIELD_NAMES,
	        -KEY_FIELDS   => ['username'],
=======
	        -TABLE        => 'voltamp_tb',
	        -USERNAME     => $AUTH_MSQL_USER_NAME,
	        -PASSWORD     => $MySQLPW,
	        -FIELD_NAMES  => \@DATASOURCE_FIELD_NAMES,
	        -KEY_FIELDS   => ['record id'],
>>>>>>> CSC
	        -FIELD_TYPES  => {
	            record_id        => 'Autoincrement',
                    datetime         => 
                                    [
                                     -TYPE  => "Date",
                                     -STORAGE => 'y-m-d H:M:S',
                                     -DISPLAY => 'y-m-d H:M:S',
                                    ],
<<<<<<< HEAD
	        },
	);

    }

######################################################################
#                          project db  SETUP                              #
######################################################################

my @PROJECT_DATASOURCE_FIELD_NAMES = qw(
        record_id
        status
        project_code
        project_name
        project_size
        estimated_man_hours
        developer_name
        client_name
        comments        
        username_of_poster
        group_of_poster
        date_time_posted
);

my	@PROJ_DATASOURCE_CONFIG_PARAMS;

if ($site eq "file"){
	@PROJ_DATASOURCE_CONFIG_PARAMS = (
    -TYPE                       => 'File',
    -FILE                       => "$APP_DATAFILES_DIRECTORY/$SiteName._project_tb.dat",
    -FIELD_DELIMITER            => '|',
    -COMMENT_PREFIX             => '#',
    -CREATE_FILE_IF_NONE_EXISTS => 1,
    -FIELD_NAMES                => \@DATASOURCE_FIELD_NAMES,
    -KEY_FIELDS                 => ['record_id'],
    -FIELD_TYPES                => {
                                    record_id        => 'Autoincrement',
                                    datetime         =>
                                    [
                                     -TYPE  => "Date",
                                     -STORAGE => 'y-m-d H:M:S',
                                     -DISPLAY => 'y-m-d H:M:S',
                                    ],
                                   },
);
}else{
	@PROJ_DATASOURCE_CONFIG_PARAMS = (
	        -TYPE         => 'DBI',
	        -DBI_DSN      => $DBI_DSN,
	        -TABLE        => $ProjectTableName,
	        -USERNAME     => $AUTH_MSQL_USER_NAME,
	        -PASSWORD     => $MySQLPW,
	        -FIELD_NAMES  => \@PROJECT_DATASOURCE_FIELD_NAMES,
	        -KEY_FIELDS   => ['username'],
	        -FIELD_TYPES  => {
	            record_id        => 'Autoincrement'
	        },
	);
}

my @BUYCAT_DATASOURCE_FIELD_NAMES = qw(
        record_id
        status
        category
        subcategory
        sitename
        display_value
        client_name
        comments        
        username_of_poster
        group_of_poster
        date_time_posted
);

my  @BUYCAT_DATASOURCE_CONFIG_PARAMS = (
	        -TYPE         => 'DBI',
	        -DBI_DSN      => $DBI_DSN,
	        -TABLE        => $DropListName,
	        -USERNAME     => $AUTH_MSQL_USER_NAME,
	        -PASSWORD     => $MySQLPW,
	        -FIELD_NAMES  => \@BUYCAT_DATASOURCE_FIELD_NAMES,
	        -KEY_FIELDS   => ['category'],
	        -FIELD_TYPES  => {
	            record_id        => 'Autoincrement',
                    datetime         => 
                                    [
                                     -TYPE  => "Date",
                                     -STORAGE => 'y-m-d H:M:S',
                                     -DISPLAY => 'y-m-d H:M:S',
                                    ],
	        },
	);
=======
                                   },
);
   }
>>>>>>> CSC


my @DATASOURCE_CONFIG_PARAMS = (
    -BASIC_DATASOURCE_CONFIG_PARAMS     => \@BASIC_DATASOURCE_CONFIG_PARAMS,
<<<<<<< HEAD
    -BUYCAT_DATASOURCE_CONFIG_PARAMS  => \@BUYCAT_DATASOURCE_CONFIG_PARAMS,
    -PROJECT_DATASOURCE_CONFIG_PARAMS   => \@PROJ_DATASOURCE_CONFIG_PARAMS,
    -AUTH_USER_DATASOURCE_CONFIG_PARAMS => \@AUTH_USER_DATASOURCE_PARAMS
);

my @PROJECT_DATASOURCE_CONFIG_PARAMS = (
    -PROJECT_DATASOURCE_CONFIG_PARAMS     => \@PROJ_DATASOURCE_CONFIG_PARAMS,
);

######################################################################
#                          MAILER SETUP                              #
######################################################################
my @MAIL_CONFIG_PARAMS = 
    (
     -TYPE         => 'Sendmail'
    );

my @EMAIL_DISPLAY_FIELDS = 
    qw(
       subject
       category
       start_date
       end_date
       description
       estimated_man_hours 
      );
=======
    -AUTH_USER_DATASOURCE_CONFIG_PARAMS => \@AUTH_USER_DATASOURCE_PARAMS
);

######################################################################
#                          MAILER SETUP                              #
######################################################################
           
my @MAIL_CONFIG_PARAMS = (     
    -TYPE         => 'Sendmail'
);

my @EMAIL_DISPLAY_FIELDS = qw(
        status
        Volts
        Amps$CSS_VIEW_URL  = $SetupVariables->{-CSS_VIEW_NAME};

        comments        
);
>>>>>>> CSC

my @DELETE_EVENT_MAIL_SEND_PARAMS = (
    -FROM     =>  $SESSION->getAttribute(-KEY =>
'auth_email')||$mail_from,
    -TO       => $mail_to,
    -REPLY_TO => $mail_replyto,
<<<<<<< HEAD
    -SUBJECT  => $APP_NAME_TITLE." Delete"
=======
    -SUBJECT  => $APP_NAME_TITLE.' Delete'
>>>>>>> CSC
);

my @ADD_EVENT_MAIL_SEND_PARAMS = (
    -FROM     =>  $SESSION->getAttribute(-KEY =>
'auth_email')||$mail_from,
<<<<<<< HEAD
    -TO       => $mail_to.','.$mail_to_discussion,
    -BCC      => $mail_list_bcc,
    -REPLY_TO => $mail_replyto,
    -SUBJECT  => $APP_NAME_TITLE." Addition"
);

my @MODIFY_EVENT_MAIL_SEND_PARAMS = (
    -FROM     => $SESSION->getAttribute(-KEY =>
'auth_email')||$mail_from,
    -TO       => $mail_to.','.$mail_to_discussion,
    -REPLY_TO => $mail_replyto,
    -SUBJECT  => $APP_NAME_TITLE." Modification"
);

=======
    -TO       => $mail_to,
    -REPLY_TO => $mail_replyto,
    -SUBJECT  => $APP_NAME_TITLE.' Addition'
);

my @MODIFY_EVENT_MAIL_SEND_PARAMS = (
    -FROM     =>  $SESSION->getAttribute(-KEY =>
'auth_email')||$mail_from,
    -TO       => $mail_to,
    -REPLY_TO => $mail_replyto,
    -SUBJECT  => $APP_NAME_TITLE.' Modification'
);


>>>>>>> CSC
my @MAIL_SEND_PARAMS = (
    -DELETE_EVENT_MAIL_SEND_PARAMS => \@DELETE_EVENT_MAIL_SEND_PARAMS,
    -ADD_EVENT_MAIL_SEND_PARAMS    => \@ADD_EVENT_MAIL_SEND_PARAMS,
    -MODIFY_EVENT_MAIL_SEND_PARAMS => \@MODIFY_EVENT_MAIL_SEND_PARAMS
);

##################################################################
#                         LOGGING SETUP                          #
##################################################################

my @LOG_CONFIG_PARAMS = (
    -TYPE             => 'File',
    -LOG_FILE         => "$APP_DATAFILES_DIRECTORY/$APP_NAME.log",
    -LOG_ENTRY_SUFFIX => '|' . _generateEnvVarsString() . '|',
<<<<<<< HEAD
    -LOG_ENTRY_PREFIX =>  $APP_NAME_TITLE.' |'
=======
    -LOG_ENTRY_PREFIX => '$APP_NAME_TITLE|'
>>>>>>> CSC
);

sub _generateEnvVarsString {
    my @env_values;
    
    my $key;
    foreach $key (keys %ENV) {
        push (@env_values, "$key=" . $ENV{$key});
    }   
    return join ("\|", @env_values);
}   
<<<<<<< HEAD
   
=======
  
>>>>>>> CSC
######################################################################
#                          VIEW SETUP                                #
######################################################################

<<<<<<< HEAD
my @VALID_VIEWS = 
    qw(
       BCHPACSSView
       ECFCSSView
       ApisCSSView
       CSPSCSSView
       CSCCSSView

       DetailsRecordView
       BasicDataView
       ContactView
       BuySellHomeView

       AddRecordView
       AddRecordConfirmationView
       AddAcknowledgementView

       DeleteRecordConfirmationView
       DeleteAcknowledgementView

       ModifyRecordView
       ModifyRecordConfirmationView
       ModifyAcknowledgementView

       ProductView
       PowerSearchFormView
       OptionsView
       LogoffView
       PrivacyView
       CellLogView
       BuyCatagoryView
       JobView
       VoltAmpView
      );

my @ROW_COLOR_RULES = (
);

my @VIEW_DISPLAY_PARAMS = (
=======
my @VALID_VIEWS = qw(
       CSPSCSSView
       CSCCSSView
       CAPCSSView
       VitalVicCSSView
       ApisCSSView
       ENCYCSSView
       BCAFCSSView
       AddAcknowledgementView
       AddRecordConfirmationView
       DeleteRecordConfirmationView
       DeleteAcknowledgementView
       ModifyAcknowledgementView
       ModifyRecordConfirmationView
       SessionTimeoutErrorView
       AddRecordView
       PowerSearchFormView
       BasicDataView
       DetailsRecordView
       ModifyRecordView
       LogoffView
       OptionsView
       InventoryProjectionView
       YardsView
       FeedingView 	
       InventoryView      
);	


my @ROW_COLOR_RULES = (
   {'Volts' => [qw(Requested 99CC99)]},
   {'status' => [qw(In-Process CC9999)]},
   {'status' => [qw(Delivered CC9999)]}
);

my @FIELD_COLOR_RULES = (
   {'Volts' => [qw(Large BLUE)]},
   {'Amps' => [qw(Small ORANGE)]}
);


my @VIEW_DISPLAY_PARAMS = (
    -ROW_COLOR_RULES         => \@ROW_COLOR_RULES,
    -FIELD_COLOR_RULES       => \@FIELD_COLOR_RULES,
>>>>>>> CSC
    -APPLICATION_LOGO               => $app_logo,
    -APPLICATION_LOGO_HEIGHT        => $app_logo_height,
    -APPLICATION_LOGO_WIDTH         => $app_logo_width,
    -APPLICATION_LOGO_ALT           => $app_logo_alt,
<<<<<<< HEAD
	 -FAVICON                        => $FAVICON,
	 -ANI_FAVICON                    => $ANI_FAVICON,
	 -FAVICON_TYPE                   => $FAVICON_TYPE,
    -DEFAULT_CHARSET                => $DEFAULT_CHARSET,
    -DISPLAY_FIELDS                 => [qw(
        category
        item_name
        price
        url
        location
        )],
    -DOCUMENT_ROOT_URL       => $DOCUMENT_ROOT_URL,
=======
    -DOCUMENT_ROOT_URL       => $DOCUMENT_ROOT_URL,
    -IMAGE_ROOT_URL          => $IMAGE_ROOT_URL,
    -HTTP_HEADER_PARAMS      => $HTTP_HEADER_PARAMS,
    -LINK_TARGET             => $LINK_TARGET,
    -SCRIPT_DISPLAY_NAME     => $APP_NAME_TITLE,
    -SCRIPT_NAME             => $CGI->script_name(),
>>>>>>> CSC
    -EMAIL_DISPLAY_FIELDS    => \@EMAIL_DISPLAY_FIELDS,
    -FIELDS_TO_BE_DISPLAYED_AS_EMAIL_LINKS => [qw(
        email
    )],
    -FIELDS_TO_BE_DISPLAYED_AS_LINKS => [qw(
        url
    )],
<<<<<<< HEAD
    -FIELDS_TO_BE_DISPLAYED_AS_HTML_TAG => [qw(
        description
	     item_name
	     comments
    )],
    -FIELDS_TO_BE_DISPLAYED_AS_MULTI_LINE_TEXT => [qw(
        description
	     item_name
 	comments
   )],
    -FIELD_NAME_MAPPINGS     => {
        'category'=> 'Catagory',
        'description' => 'Description',
        'Volts'       => 'Volts',
        'location'    => 'location',
        'BatteryCode' => 'BatteryCode',
        'CellCode'    => 'CellCode',
        'Amps'        => 'Amps',
        'Temp'    => 'Temperature',
        },
    -HOME_VIEW               => 'CellLogView',
    -IMAGE_ROOT_URL          => $IMAGE_ROOT_URL,
    -LINK_TARGET             => $LINK_TARGET,
    -HTTP_HEADER_PARAMS      => $HTTP_HEADER_PARAMS,
    -HTTP_HEADER_KEYWORDS    => $HTTP_HEADER_KEYWORDS,
    -HTTP_HEADER_DESCRIPTION => $HTTP_HEADER_DESCRIPTION,
    -ROW_COLOR_RULES         => \@ROW_COLOR_RULES,
    -SCRIPT_DISPLAY_NAME     => $APP_NAME_TITLE,
    -SITE_DISPLAY_NAME       => $SITE_DISPLAY_NAME,
    -SCRIPT_NAME             => $CGI->script_name(),
    -SELECTED_DISPLAY_FIELDS => $columnstoview,
    -SORT_FIELDS             => $SortFields,
    -VERSION                 => $version,
);  

######################################################################
#                           DATE TIME SETUP                          #
######################################################################

my @DATETIME_CONFIG_PARAMS = 
    (
     -TYPE => (HAS_CLASS_DATE ? 'ClassDate' : 'DateManip'),
    );
=======
    -FIELDS_TO_BE_DISPLAYED_AS_MULTI_LINE_TEXT => [qw(
        body
    )],
    -HOME_VIEW               => $homeviewname,
    -FIELD_NAME_MAPPINGS   => {
        site               => 'sitecode',
        Time               => 'Time',
        BatteryCode        => 'BatteryCode',
        CellCode           => 'CellCode',
        Volts              => 'Volts',
        Amps               => 'Amperage',
        comments           => 'Comments'
        },
    -DISPLAY_FIELDS        => [qw(
        sitename 
        Time      
        Volts
        Amps
        BatteryCode
        CellCode
        Comments
        )],
    -SORT_FIELDS        => [qw(
        sitename
        Volts
        Amps
        )],
    -SELECTED_DISPLAY_FIELDS        => [qw(
        sitename
        Time
        BatteryCode
        CellCode       
        Volts
        Amps
        Comments
        )],        

);  
>>>>>>> CSC

######################################################################
#                           FILTER SETUP                             #
######################################################################

my @HTMLIZE_FILTER_CONFIG_PARAMS = (
<<<<<<< HEAD
    -TYPE                          => 'HTMLize',
    -CONVERT_DOUBLE_LINEBREAK_TO_P => 1,
    -CONVERT_LINEBREAK_TO_BR       => 1,
=======
    -TYPE            => 'HTMLize',
    -CONVERT_DOUBLE_LINEBREAK_TO_P => 1,
    -CONVERT_LINEBREAK_TO_BR => 1,
>>>>>>> CSC
);

my @CHARSET_FILTER_CONFIG_PARAMS = (
    -TYPE            => 'CharSet'
);

<<<<<<< HEAD

my @EMBED_FILTER_CONFIG_PARAMS = (
    -TYPE            => 'Embed',
    -ENABLE          => $CGI->param('embed') || 0
=======
my @EMBED_FILTER_CONFIG_PARAMS = (
    -TYPE            => 'Embed',
    -ENABLE          => 0
>>>>>>> CSC
);

my @VIEW_FILTERS_CONFIG_PARAMS = (
     \@HTMLIZE_FILTER_CONFIG_PARAMS,
     \@CHARSET_FILTER_CONFIG_PARAMS,
     \@EMBED_FILTER_CONFIG_PARAMS
<<<<<<< HEAD
); 
=======
);

>>>>>>> CSC

######################################################################
#                      ACTION/WORKFLOW SETUP                         #
######################################################################
<<<<<<< HEAD

# note: Default::DefaultAction must! be the last one
my @ACTION_HANDLER_LIST =
    qw(
       Default::SetSessionData
       Default::DisplayCSSViewAction

       Default::PopulateInputWidgetDefinitionListWithBuyCategoryWidgetAction
       CSC::ProcessShowAllOpenToDosAction
       Apis::ProcessShowBillsRecordsAction
       Default::DisplayDetailsRecordViewAction

       Default::DisplayDeleteFormAction
       Default::ProcessDeleteRequestAction
       Default::DisplayDeleteRecordConfirmationAction

       Default::DisplayModifyFormAction
       BuyAndSell::ProcessModifyRequestAction
       Default::DisplayModifyRecordConfirmationAction

       Default::DisplayAddFormAction
       BuyAndSell::ProcessAddRequestAction
       Default::DisplayAddRecordConfirmationAction

       Default::DisplaySimpleSearchResultsAction
       Default::DisplayOptionsFormAction
       Default::DisplayPowerSearchFormAction
       Default::PerformPowerSearchAction

       Default::PerformLogonAction
       Default::PerformLogoffAction

       Default::DisplayViewAllRecordsAction
       Default::DefaultAction	 
  
      );


my @ACTION_HANDLER_ACTION_PARAMS = (
    -ACTION_HANDLER_LIST                    => \@ACTION_HANDLER_LIST,
    -ADD_ACKNOWLEDGEMENT_VIEW_NAME          => 'AddAcknowledgementView',
    -ADD_EMAIL_BODY_VIEW                    => 'AddEventEmailView',
    -ADD_FORM_VIEW_NAME                     => 'AddRecordView',
    -AFFILIATE_NUMBER                       => $Affiliate,
    -ALLOW_ADDITIONS_FLAG                   => 1,
    -ALLOW_MODIFICATIONS_FLAG               => 1,
    -ALLOW_DELETIONS_FLAG                   => 1,
    -ALLOW_DUPLICATE_ENTRIES                => 0,
    -ALLOW_USERNAME_FIELD_TO_BE_SEARCHED    => 1,
    -APP_NAME                               => $APP_NAME,
    -APPLICATION_SUB_MENU_VIEW_NAME         => $apsubmenu,
    -OPTIONS_FORM_VIEW_NAME                 => 'OptionsView',
    -AUTH_MANAGER_CONFIG_PARAMS             => \@AUTH_MANAGER_CONFIG_PARAMS,
    -ADD_RECORD_CONFIRMATION_VIEW_NAME      => 'AddRecordConfirmationView',
    -BASIC_DATA_VIEW_NAME                   => 'VoltAmpView',
    -BATTERY                                => $BatteryCode,
    -DEFAULT_ACTION_NAME                    => 'DisplayDayViewAction',
    -CGI_OBJECT                             => $CGI,
    -CSS_VIEW_URL                           => $CSS_VIEW_URL,
    -CSS_VIEW_NAME                          => $CSS_VIEW_NAME,
    -DATASOURCE_CONFIG_PARAMS               => \@DATASOURCE_CONFIG_PARAMS,
    -DELETE_ACKNOWLEDGEMENT_VIEW_NAME       => 'DeleteAcknowledgementView',
    -DELETE_RECORD_CONFIRMATION_VIEW_NAME   => 'DeleteRecordConfirmationView',
    -RECORDS_PER_PAGE_OPTS                  => [5, 10, 25, 50, 100],
    -MAX_RECORDS_PER_PAGE                   => $RecordsToDisplay || 10,
    -SORT_FIELD1                            => $SortField1,
    -SORT_FIELD2                            => $SortField2,
    -SORT_DIRECTION                         => $SortDirection|| 'DESC',
#   -SORT_DIRECTION                         => 'DESC',
    -DELETE_FORM_VIEW_NAME                  => 'DetailsRecordView',
    -DELETE_EMAIL_BODY_VIEW                 => 'DeleteEventEmailView',
    -DETAILS_VIEW_NAME                      => 'DetailsRecordView',
    -GROUP_OF_POSTER                        => $GROUP_OF_POSTER,
    -DATA_HANDLER_MANAGER_CONFIG_PARAMS     => \@DATA_HANDLER_MANAGER_CONFIG_PARAMS,
    -DISPLAY_ACKNOWLEDGEMENT_ON_ADD_FLAG    => 1,
    -DISPLAY_ACKNOWLEDGEMENT_ON_DELETE_FLAG => 1,
    -DISPLAY_ACKNOWLEDGEMENT_ON_MODIFY_FLAG => 1,
    -DISPLAY_CONFIRMATION_ON_ADD_FLAG       => 1,
    -DISPLAY_CONFIRMATION_ON_DELETE_FLAG    => 1,
    -DISPLAY_CONFIRMATION_ON_MODIFY_FLAG    => 1,
=======
#Apis::PopulateInputWidgetDefinitionListWithCurrentQueenCodeWidgetAction

my @ACTION_HANDLER_LIST = 
    qw(
       Default::SetSessionData
       Default::DisplayCSSViewAction
       Default::DisplaySessionTimeoutErrorAction
       Default::PerformLogoffAction
       Default::PerformLogonAction
       Default::DisplayOptionsFormAction
       Default::DownloadFileAction
       Default::DisplayAddFormAction
       Default::DisplayAddRecordConfirmationAction
       Default::ProcessAddRequestAction
       Default::DisplayDeleteFormAction
       Default::DisplayDeleteRecordConfirmationAction
       Default::ProcessDeleteRequestAction
       Default::DisplayModifyFormAction
       Default::ProcessModifyRequestAction
       Default::DisplayModifyRecordConfirmationAction
       Default::DisplayPowerSearchFormAction
       Default::DisplayDetailsRecordViewAction
       Default::DisplayViewAllRecordsAction
       Default::DisplaySimpleSearchResultsAction
       Default::PerformPowerSearchAction
       Default::HandleSearchByUserAction
       Default::DisplayBasicDataViewAction
       Default::DefaultAction
      );

my @ACTION_HANDLER_ACTION_PARAMS = (
    -ACTION_HANDLER_LIST                    => \@ACTION_HANDLER_LIST,
    -ADD_ACKNOWLEDGEMENT_VIEW_NAME          => 'AddAcknowledgementView',
    -DELETE_ACKNOWLEDGEMENT_VIEW_NAME       => 'DeleteAcknowledgementView',
    -MODIFY_ACKNOWLEDGEMENT_VIEW_NAME       => 'ModifyAcknowledgementView',
    -POWER_SEARCH_VIEW_NAME                 => 'PowerSearchFormView',
    -ADD_RECORD_CONFIRMATION_VIEW_NAME      => 'AddRecordConfirmationView',
    -MODIFY_RECORD_CONFIRMATION_VIEW_NAME   => 'ModifyRecordConfirmationView',
    -DELETE_RECORD_CONFIRMATION_VIEW_NAME   => 'DeleteRecordConfirmationView',
    -ALLOW_ADDITIONS_FLAG                   => 1,
    -ALLOW_DELETIONS_FLAG                   => 1,
    -ALLOW_MODIFICATIONS_FLAG               => 1,
    -ALLOW_DUPLICATE_ENTRIES                => 0,
    -ADD_EMAIL_BODY_VIEW                    => 'AddEventEmailView',
    -ADD_FORM_VIEW_NAME                     => 'AddRecordView',
    -AUTH_MANAGER_CONFIG_PARAMS             => \@AUTH_MANAGER_CONFIG_PARAMS,
    -APPLICATION_SUB_MENU_VIEW_NAME         => 'ApplicationSubMenuView',
    -OPTIONS_FORM_VIEW_NAME                 => 'OptionsView',
    -BASIC_DATA_VIEW_NAME                   => 'BasicDataView',
    -CGI_OBJECT                             =>  $CGI,
    -CSS_VIEW_URL                           => $CSS_VIEW_URL,
    -CSS_VIEW_NAME                          => $CSS_VIEW_NAME,
    -DATA_HANDLER_MANAGER_CONFIG_PARAMS     => \@DATA_HANDLER_MANAGER_CONFIG_PARAMS,
    -DATASOURCE_CONFIG_PARAMS               => \@DATASOURCE_CONFIG_PARAMS,
    -DISPLAY_ACKNOWLEDGEMENT_ON_ADD_FLAG    => 0,
    -DISPLAY_ACKNOWLEDGEMENT_ON_DELETE_FLAG => 1,
    -DISPLAY_ACKNOWLEDGEMENT_ON_MODIFY_FLAG => 0,
    -DISPLAY_CONFIRMATION_ON_ADD_FLAG       => 0,
    -DISPLAY_CONFIRMATION_ON_DELETE_FLAG    => 1,
    -DISPLAY_CONFIRMATION_ON_MODIFY_FLAG    => 0,
    -DETAILS_VIEW_NAME                      => 'DetailsRecordView',
    -DELETE_FORM_VIEW_NAME                  => 'BasicDataView',
    -DELETE_EMAIL_BODY_VIEW                 => 'DeleteEventEmailView',
    -DEFAULT_SORT_FIELD1                    => 'status',
    -DEFAULT_SORT_FIELD2                    => 'yard_name',
>>>>>>> CSC
    -ENABLE_SORTING_FLAG                    => 1,
    -HAS_MEMBERS                            => $HasMembers,
    -HIDDEN_ADMIN_FIELDS_VIEW_NAME          => 'HiddenAdminFieldsView',
    -INPUT_WIDGET_DEFINITIONS               => \@INPUT_WIDGET_DEFINITIONS,
<<<<<<< HEAD
    -BASIC_INPUT_WIDGET_DISPLAY_COLSPAN     => 4,
    -KEY_FIELD                              => 'record_id',
    -LOGOFF_VIEW_NAME                       => 'LogoffView',
    -URL_ENCODED_ADMIN_FIELDS_VIEW_NAME     => 'URLEncodedAdminFieldsView',
    -LAST_UPDATE                            => $last_update,
    -LOCAL_IP                               => $LocalIp,
    -LOG_CONFIG_PARAMS                      => \@LOG_CONFIG_PARAMS,
    -MODIFY_ACKNOWLEDGEMENT_VIEW_NAME       => 'ModifyAcknowledgementView',
    -MODIFY_RECORD_CONFIRMATION_VIEW_NAME   => 'ModifyRecordConfirmationView',
    -MAIL_CONFIG_PARAMS                     => \@MAIL_CONFIG_PARAMS,
    -MESSAGE_FOOTER                         => $footer,
    -MAIL_SEND_PARAMS                       => \@MAIL_SEND_PARAMS,
    -MODIFY_FORM_VIEW_NAME                  => 'ModifyRecordView',
    -MODIFY_EMAIL_BODY_VIEW                 => 'ModifyEventEmailView',
    -POWER_SEARCH_VIEW_NAME                 => 'PowerSearchFormView',
    -REQUIRE_AUTH_FOR_SEARCHING_FLAG        => 0,
=======
    -URL_ENCODED_ADMIN_FIELDS_VIEW_NAME     => 'URLEncodedAdminFieldsView',
    -LOG_CONFIG_PARAMS                      => \@LOG_CONFIG_PARAMS,
    -LOGOFF_VIEW_NAME                       => 'LogoffView',
    -MAIL_CONFIG_PARAMS                     => \@MAIL_CONFIG_PARAMS,
    -MAIL_SEND_PARAMS                       => \@MAIL_SEND_PARAMS,
    -MODIFY_FORM_VIEW_NAME                  => 'ModifyRecordView',
    -MODIFY_EMAIL_BODY_VIEW                 => 'ModifyEventEmailView',
    -REQUIRE_AUTH_FOR_SEARCHING_FLAG        => 1,
>>>>>>> CSC
    -REQUIRE_AUTH_FOR_ADDING_FLAG           => 1,
    -REQUIRE_AUTH_FOR_MODIFYING_FLAG        => 1,
    -REQUIRE_AUTH_FOR_DELETING_FLAG         => 1,
    -REQUIRE_AUTH_FOR_VIEWING_DETAILS_FLAG  => 0,
<<<<<<< HEAD
    -REQUIRE_MATCHING_USERNAME_FOR_MODIFICATIONS_FLAG => 1,
    -REQUIRE_MATCHING_GROUP_FOR_MODIFICATIONS_FLAG    => 0,
    -REQUIRE_MATCHING_USERNAME_FOR_DELETIONS_FLAG     => 1,
    -REQUIRE_MATCHING_GROUP_FOR_DELETIONS_FLAG        => 0,
    -REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG     => 0,
    -REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG        => 0,
    -SEND_EMAIL_ON_DELETE_FLAG              => 1,
    -SEND_EMAIL_ON_MODIFY_FLAG              => 1,
    -SEND_EMAIL_ON_ADD_FLAG                 => 1,
    -SESSION_OBJECT                         => $SESSION,
    -SESSION_TIMEOUT_VIEW_NAME              => 'SessionTimeoutErrorView',
    -TEMPLATES_CACHE_DIRECTORY              => $TEMPLATES_CACHE_DIRECTORY,
    -VALID_VIEWS                            => \@VALID_VIEWS,
    -VIEW_DISPLAY_PARAMS                    => \@VIEW_DISPLAY_PARAMS,
    -VIEW_FILTERS_CONFIG_PARAMS             => \@VIEW_FILTERS_CONFIG_PARAMS,
    -VIEW_LOADER                            => $VIEW_LOADER,
    -SIMPLE_SEARCH_STRING                   => $CGI->param('simple_search_string') || "",
    -FIRST_RECORD_ON_PAGE                   => $CGI->param('first_record_to_display') || 0,
    -LAST_RECORD_ON_PAGE                    => $CGI->param('first_record_to_display') || "0",
    -SITE_NAME                              => $SiteName,
    -SITE_LAST_UPDATE                       => $site_update,
    -PAGE_TOP_VIEW                          =>  $page_top_view ,
    -PAGE_LEFT_VIEW                         =>  $page_left_view,
    -PAGE_BOTTOM_VIEW                       =>  $page_bottom_view,
    -SELECT_FORUM_VIEW		            => 'SelectForumView',
    -DATETIME_CONFIG_PARAMS                 => \@DATETIME_CONFIG_PARAMS,
    -ACTION_HANDLER_PLUGINS                 => \%ACTION_HANDLER_PLUGINS,
=======
    -REQUIRE_MATCHING_USERNAME_FOR_MODIFICATIONS_FLAG => $match_use_mod,
    -REQUIRE_MATCHING_USERNAME_FOR_DELETIONS_FLAG     => 0,
    -REQUIRE_MATCHING_GROUP_FOR_MODIFICATIONS_FLAG    => 0,
    -REQUIRE_MATCHING_GROUP_FOR_DELETIONS_FLAG        => 0,
    -REQUIRE_MATCHING_USERNAME_FOR_SEARCHING_FLAG     => $match_user_search,
    -REQUIRE_MATCHING_GROUP_FOR_SEARCHING_FLAG        =>
$match_group_search,
    -SEND_EMAIL_ON_DELETE_FLAG             => 0,
    -SEND_EMAIL_ON_MODIFY_FLAG             => 0,
    -SEND_EMAIL_ON_ADD_FLAG                => 0,
    -SESSION_OBJECT                        => $SESSION,
    -SESSION_TIMEOUT_VIEW_NAME             => 'SessionTimeoutErrorView',
    -SIMPLE_SEARCH_BOX_VIEW_NAME            => 'SimpleSearchBoxView',
    -VIEW_FILTERS_CONFIG_PARAMS            => \@VIEW_FILTERS_CONFIG_PARAMS,
    -VIEW_DISPLAY_PARAMS                   => \@VIEW_DISPLAY_PARAMS,
    -TEMPLATES_CACHE_DIRECTORY              => $TEMPLATES_CACHE_DIRECTORY,
    -VALID_VIEWS                           => \@VALID_VIEWS,
    -VIEW_LOADER                           => $VIEW_LOADER,
    -RECORDS_PER_PAGE_OPTS                  => [5, 10, 25, 50, 100],
    -MAX_RECORDS_PER_PAGE                   => $CGI->param('records_per_page') || 100,
    -SORT_FIELD1                            => $CGI->param('sort_field1') || 'BatteryCode',
    -SORT_FIELD2                            => $CGI->param('sort_field2') || 'time',
    -SORT_DIRECTION                         => $CGI->param('sort_direction') || 'ASC',
    -SIMPLE_SEARCH_STRING                   => $CGI->param('simple_search_string') || "",
    -FIRST_RECORD_ON_PAGE                   => $CGI->param('first_record_to_display') || 0,
    -LAST_RECORD_ON_PAGE                    => $CGI->param('first_record_to_display') || "0",
    -KEY_FIELD                              => 'record_id',
    -SITE_NAME                              => $SiteName,
    -PAGE_TOP_VIEW           =>  $CGI->param('page_top_view') ||  $page_top_view ,
    -LEFT_PAGE_VIEW          =>  $CGI->param('left_page_view') || $left_page_view,
    -PAGE_BOTTOM_VIEW        =>  $CGI->param('$page_bottom_view') || $page_bottom_view,
    -BASIC_INPUT_WIDGET_DISPLAY_COLSPAN     => 2,
>>>>>>> CSC
);

######################################################################
#                      LOAD APPLICATION                              #
######################################################################

<<<<<<< HEAD
my $APP = Extropia::Core::App::DBApp->new(
=======
my $APP = new Extropia::Core::App::DBApp(
>>>>>>> CSC
    -ROOT_ACTION_HANDLER_DIRECTORY => "../ActionHandler",
    -ACTION_HANDLER_ACTION_PARAMS => \@ACTION_HANDLER_ACTION_PARAMS,
    -ACTION_HANDLER_LIST          => \@ACTION_HANDLER_LIST,
    -VIEW_DISPLAY_PARAMS          => \@VIEW_DISPLAY_PARAMS
    ) or die("Unable to construct the application object in " . 
<<<<<<< HEAD
             $CGI->script_name() .  ". Please contact the webmaster.");

#print "Content-type: text/html\n\n";
print $APP->execute();
=======
             $CGI->script_name() . ". Please contact the webmaster.");

print $APP->execute();

>>>>>>> CSC
