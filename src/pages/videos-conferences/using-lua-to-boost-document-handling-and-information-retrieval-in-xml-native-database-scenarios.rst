=================================================================================================
Using Lua to boost document handling and information retrieval in XML Native Database scenarios
=================================================================================================

:url: conferences/grand-public/using-lua-to-boost-document-handling-and-information-retrieval-in-xml-native-database-scenarios.html
:save_as: conferences/grand-public/using-lua-to-boost-document-handling-and-information-retrieval-in-xml-native-database-scenarios.html
:video_url: http://stream.toulibre.org/cdl2013/lua-samedi/capoccia-tirabassi-lua-boost-document-handling
:speakers: Valerio Capoccia and Roberto Tirabassi
:licence: CC0
:licence_url: http://creativecommons.org/publicdomain/zero/1.0/
:template: conference

.. html::

 <p>Our primary target was integrate a scripting language to delegate specific operation on data to something else than the engine. The specific target, required very intimate integration with a multitude of features Document/Object Oriented belonging to the engine and at the same time a great simplicity and flexibility of development. By placing the look at the panorama of scripting languages that could lend themselves for this purpose, whereas the integration would take place with modules fully implemented in C/C++, Lua language has soon proved our right choice. It is widespread and is used in many different areas. It has a wide extensibility as well a wide range of functionality and libraries already available, and is designed to suit a multitude of our needs. In its declination LuaJIT, also offers a level of performance further advanced. Our implementation of Lua in eXtraWay provides an executor of scripts, organized into packages in java style, which can be invoked explicitly (Stored Procedures) or run automatically inside the engine(Triggers) and who are able to take advantage each other through a simple inclusion system. We have developed specific packages for individual databases eXtraWay in which it was necessary to carry out specific and tricky operations on documents and indices. Were also developed generic library to perform common operations on documents through Lua, reusable in multiple scenarios. Each package refers to a dynamic library specifically designed allowing you to use the functionality of the server invocandole directly from Lua scripts built. so you can create records, save them, search them, operate on lists of records and their abstract, load the XML content and perform multiple operations on the same structure including managing digital content associated with them. You can also perform batch external and different solutions have been implemented for the management of large amounts of data in memory and on file.</p>

