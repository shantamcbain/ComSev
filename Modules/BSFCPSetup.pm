package BSFCPSetup;


use strict;
use CGI::Carp qw(fatalsToBrowser);
# $site = 'file';
#my $datesourcetype = 'MySQL';
my $datesourcetype = 'file';

sub new {
my $package    = shift;
my $UseModPerl = shift || 0;


my $self = {
            -SITE_LAST_UPDATE       => 'April 14, 2012',
 	    -SHOP	                    => "cs",
            -SITE_DISPLAY_NAME          => 'Bee S.A.F.E. Fortunes Creek Project',
	    -HOME_VIEW              => 'PageView',
	    -BASIC_DATA_VIEW        => 'BasicDataView',
	    -APP_LOGO               => '/images/apis/bee.gif',
	    -APP_LOGO_ALT           => 'apis Logo',
	    -APP_LOGO_WIDTH         => '60',
	    -APP_LOGO_HEIGHT        => '60',
       -AUTH_TABLE             => 'bsfcp_user_auth_tb',
	    -FAVICON                => '/images/apis/favicon.ico',
	    -ANI_FAVICON            => '/images/apis/extra/animated_favicon.gif',
	    -FAVICON_TYPE           => '/image/x-icon',
	    -CSS_VIEW_NAME          => "/styles/apis.css",
       -DEFAULT_CHARSET        => 'ISO-8859-1', 
	    -PAGE_TOP_VIEW          => 'PageTopView',
	    -PAGE_BOTTOM_VIEW       => 'PageBottomView',
	    -PAGE_LEFT_VIEW         => 'LeftPageView',
	    -MAIL_FROM              => 'shanta@grindrodbc.com',
	    -MAIL_TO                => 'shanta@grindrodbc.com',
		 -MAIL_TO_ADMIN          => 'support@grindrodbc.com',
       -MAIL_REPLYTO           => 'beemasters@grindrodbc.com',
	    -MAIL_TO_USER           => 'beemaster_user_list@list.grindrodbc.com',
	    -MAIL_TO_DISCUSSION     => 'beemaster@list.grindrodbc.com',
	    -MAIL_LIST_BCC          => '',
	    -DOCUMENT_ROOT_URL      => '/',
	    -IMAGE_ROOT_URL         => '/images/extropia',
       -HTTP_HEADER_PARAMS     => "[-EXPIRES => '-1d']",
       -HTTP_HEADER_DESCRIPTION => "B.E.E.Safe Fortunes Creek Project, GMO Free, Pesticide Free, Sustainable Farming.  ",
       -HTTP_HEADER_KEYWORDS    => "Bees, bees, bee breeding,  bee breeding, bee keeping, beekeeping, honey, honey production, queens, apis, apis therapies, pollen, pollination, pollinators, propolus, bee pollen, pollination services, Bee mentor, ",
	    -DATASOURCE_TYPE        => $datesourcetype,
 	    -ADDITIONALAUTHUSERNAMECOMMENTS => 'Please do not use spaces.',
	    -GLOBAL_DATAFILES_DIRECTORY => "../../Datafiles",
	    -TEMPLATES_CACHE_DIRECTORY  => '/TemplatesCache',
	    -APP_DATAFILES_DIRECTORY => "../../Datafiles/Apis",
	    -NEWS_TB                 => 'apis_news_tb',
	    };



return bless $self, $package; 
}






1;
