import re
import urllib.parse

l=["Build%20for%20IOS.html","Build%20for%20Windows.html","index.html","Build%20for%20Android%20(Windows).html","Build%20for%20Android%20(MacOS).html","Add%20or%20Edit%20Server.html","Add%20servers%20for%20Android%20or%20IOS.html","Add%20Servers%20for%20Windows.html"]
for i in l:
    i=urllib.parse.unquote(i)
    print(i)
    f=open(i,"r").read()
    print (f)
   # xx=re.sub('https://my-vpn.readme.io/docs/getting-started','index.html', f)
    #xx=re.sub('https://my-vpn.readme.io/docs/build-for-android',r'Build%20for%20Android%20(Windows).html', xx)
    #xx=re.sub(r'Build%20for%20Android%20(MacOS).html',r'Build%20for%20Android%20(MacOS).html ', xx)
   # xx=re.sub('https://my-vpn.readme.io/docs/build-for-ios',r'Build%20for%20IOS.html', xx)
    #xx=re.sub('https://my-vpn.readme.io/docs/build-for-windows',r'Build%20for%20Windows.html', xx)
    #xx=re.sub('https://my-vpn.readme.io/docs/add-or-edit-server',r'Add%20or%20Edit%20Server.html', xx)
    #xx=re.sub('https://my-vpn.readme.io/docs/add-servers-for-windows',r'Add%20servers%20for%20Android%20or%20IOS.html', xx)
    #xx=re.sub('https://my-vpn.readme.io/docs/add-servers-for-ios-or-android',r'Add%20Servers%20for%20Windows.html', xx)

    #xx=re.sub('<nav><ul id="header-nav-left"><li><a href="https://my-vpn.readme.io/docs" ui-sref="docs" title="Guides" class="active">Guides</a></li><li><a href="https://my-vpn.readme.io/discuss" ui-sref="discuss" title="Discussions">Discussions</a></li></ul><ul id="header-nav-right"><li><span login="" class=""><span ng-show="user.loggedIn" class="login hub-subheader-breadcrumbs"><span class="dropdown right-dropdown"><script async="" src="//www.google-analytics.com/analytics.js"></script><script async="" src="Add%20Servers%20for%20Windows_files/analytics.js"></script><script type="text/ng-template" id="loginPopover"><div id="hub-user-dropdown" class="ns-popover-tooltip"><div class="ns-triangle"></div><div class="triangle"></div><ul><li ng-show="user.isAdmin"><a href="https://dash.readme.io/project/my-vpn/v1.0/dashboard"> <i class="fa fa-lock"></i>Admin Panel</a></li><li><a ui-sref="suggested-edits"> <i class="fa fa-edit"></i>Suggested Edits</a></li><li><a ng-href="/logout?redirect_uri={{redirect()}}" target="_self"> <i class="fa fa-power-off"></i>Log out</a></li></ul></div></script><a ns-popover="" ns-popover-trigger="click" ns-popover-theme="ns-popover-dropdown-theme" ns-popover-placement="bottom|right" ns-popover-template="loginPopover" ns-popover-timeout="-1" class="hub-breadcrumb-item dropdown-toggle ng-scope ng-binding">shanaka<i class="fa fa-chevron-down"></i></a></span></span><span ng-show="!user.loggedIn" class="login ng-hide"><a href="https://dash.readme.io/to/my-vpn" target="_self">Log In</a></span></span></li></ul></nav>',r'', xx)
    #xx=re.sub('<div searchbox="" ng-class="{full:search.full}" class="searchbox ng-scope"><input ng-model="search.query" type="text" placeholder="Search" class="search-box ng-pristine ng-untouched ng-valid"><div class="fa fa-search"></div></div>',r'', xx)
    #xx=re.sub('<div class="col-xs-3"><a ng-click="suggestedEdits.enable()" href="" class="suggestEdits"><i class="icon icon-register"></i>Suggest Edits</a></div>',r'', xx)
    #xx=re.sub('<li ng-show="ss.toc.length"><a href="" ng-click="scrollTo()" class="tocHeader"><i class="icon icon-text-align-left"></i>Table of Contents</a></li>',r'', xx)
    #xx=re.sub('<li ng-repeat="node in ss.toc" class="toc-DIV"><a href="" ng-click="scrollTo(node.data[0])" class="ng-binding">',r'<li style="display:none" ng-repeat="node in ss.toc" class="toc-DIV"><a href="" ng-click="scrollTo(node.data[0])" class="ng-binding">', xx)
    #xx=re.sub('<li><span login="" class=""><span ng-show="user.loggedIn" class="login hub-subheader-breadcrumbs"><span class="dropdown right-dropdown">',r'<li style="display:none" ><span login="" class=""><span ng-show="user.loggedIn" class="login hub-subheader-breadcrumbs"><span class="dropdown right-dropdown">', xx)

    

    #xx=re.sub('<a id="inactive-notification" href="https://dash.readme.io/project/my-vpn/v1.0/plans" class="hub-notification"><i class="icon icon-notification"></i>This site is only viewable by admins. Launch it to make it public.</a>', '',xx)

    xx=re.sub('''<a ui-sref="docs.show({'doc': 'build-for-android-1'})" href="Build%20for%20Android%20(Windows).html" ui-sref-alt="" class="text-overflow"><div class="link-title">Build for Android (MacOS)</div></a>''',r'''<a ui-sref="docs.show({'doc': 'build-for-android-1'})" href="Build%20for%20Android%20(MacOS).html" ui-sref-alt="" class="text-overflow"><div class="link-title">Build for Android (MacOS)</div></a>''', f)
   
    #xx=re.sub('html-1',r'html', f)


 
    f=open(i,"w+")
    f.write(xx)
    f.close()
