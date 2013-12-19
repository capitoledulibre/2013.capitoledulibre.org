==============================================================================
Using Lua for Responsive Programming of iOS apps
==============================================================================

:url: conferences/lua-dimanche/using-lua-for-responsive-programming-of-ios-apps.html
:save_as: conferences/lua-dimanche/using-lua-for-responsive-programming-of-ios-apps.html
:video_url: http://stream.toulibre.org/cdl2013/lua-dimanche/jumpertz-lua-responsive-programming-ios
:speakers: Jean-Luc Jumpertz
:licence: CC-By 4.0
:licence_url: http://creativecommons.org/licenses/by/4.0/
:template: conference

.. html::

 <p>Celedev has developed a live-coding-oriented development environment for iOS apps. This talk will be focused on the role of Lua as a key component of this system. It will present the reasons behind the choice of Lua and will discuss several technical aspects of the integration of Lua in a complex host operating system like iOS, including:
 <ul>
 <li> Multi-threading aspects: We will see why multi-threaded Lua is a mandatory feature in our system and we will show how to use the lua_newthread() function to run code from multiple threads within a standard Lua VM. We'll also  provide a few implementation tips &amp; tricks to avoid common traps in Lua multi-threaded implementation. 
 </li><li> Object-Oriented framework: The need for integration of Lua code with the iOS Objective C runtime has led us to design an extensive Lua Objects Framework, fully compatible with the Objective C model, but with a very Lua-ish spirit; we will give a brief overview of this framework.
 </li><li> Dynamic code update: we will discuss Celedev dynamic code update feature from the Lua implementation perspective and show how it is integrated with the Lua require() function.
 </li><li> Lua Debugger: And, as a good debugger is key for serious software development, we will put the highlight on some original features of the Celedev debugger and show the debugger integration with other features of the system discussed previously.
 </li></ul>
 This talk will be illustrated by short coding &amp; debugging demos of the Celedev Responsive Programming system on iOS devices.</p>

