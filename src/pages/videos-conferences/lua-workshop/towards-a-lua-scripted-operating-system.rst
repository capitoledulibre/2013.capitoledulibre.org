==============================================================================
Towards a Lua scripted operating system
==============================================================================

:url: conferences/lua-workshop/towards-a-lua-scripted-operating-system.html
:save_as: conferences/lua-workshop/towards-a-lua-scripted-operating-system.html
:video_url: http://stream.toulibre.org/cdl2013/lua-dimanche/cormack-lua-scripted-operating-system
:speakers: Justin Cormack
:licence: CC-By 4.0
:licence_url: http://creativecommons.org/licenses/by/4.0/
:template: conference

.. html::

 <p>Recently I have been working on a project (called "ljsyscall") to experiment with scripting operating systems in Lua. In this talk I will look at progress so far, what I have learned, and look at a roadmap towards an operating system that is scriptable entirely in Lua. Initially ljsyscall was an experiment to see what a scripting interface for Linux would look like in Lua. I started with system calls, and progress was slow, as there are lots of them and you cannot do very much with just a few. But I carried on, and then started adding facilities built on the raw system calls, such as configuration of network interfaces, security systems etc. The aim was to get to the point where an application could easily configure its whole runtime environment without needing a large infrastructure of shell scripts etc. It was partly driven by the way that the way systems boot was being made less transparent by code such as systemd which moves code into C not shell, making it harder to understand how an operating system works, while one that works in Lua should be easier to understand. The second phase, in 2013, involved more experiments, this time with NetBSD, and the NetBSD rump kernel, which allows parts of NetBSD, such as file systems and the network stack, to run in userspace, even in other operating systems, or in systems with no operating system at all such as embedded systems. Lua scripting was extended to be able to script these, with the same interface as on the operating system itself. This allowed things like booting Lua natively as a guest under Xen, without an operating system at all but with a full network stack and file system, in a couple of megabytes. Future work includes further work with NetBSD, as Lua is now a component in the core set of packages in the operating system, although it is not yet used there. NetBSD is a good complement to Lua, as it is small, portable and powerful. I intend to work towards producing a scripting interface for all the core functionality, in what will be a fruitful partnership. Other work in progress is the port of ljsyscall from LuaJIT that it originally targetted to PUC Lua, and further extensions for Linux.</p>

