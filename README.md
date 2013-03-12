Power
=====

Power is a module for python (currently supports only 2.7) that provides short, obvious and generic interface
to power capabilities of the the system. It's crossplatform and supports Mac OS X, Windows and Linux.
If your target system is missed, please creat new issue.

Since accessing power information requires acccess to system functions, it's vital to be fault tolerant.
If Power is unable to access data it needs, it returns some generic value and logs error via warnings module.
Using warnings module makes it easier for you to turn generic values into exceptions to suite your needs.

Current feature-set allows you to get the following information about power:

- Power source type

- Battery warning level

- Time remaining estimate

Since the system may have more than one battery, Power should take that into account and calculate some avergae.
Current implementation just trusts system functions where possible (Mac OS X, Windows) or uses some naive approach (Linux).
You're encouraged to review code and ask questions (by creating issues) if you feel it may affect behavior of your app.

Power also includes generic interface to create observers for changes in power configuration.
E.g. when you attach/detach battery, connect system to power wall or battery warning level is changed.  
This feature is only supported in Mac OS X. It's also possible to add support for Windows 8 on demand (create an issue).
Research is needed to add this feature to other systems.  
If your application targets multiple systems, it probably would be easier to just use timer.
Note to set timer to some reasonable long value like 5min, because Power should be efficient in terms of power (obviously).


