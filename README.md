Django JS_Store
==

A simple Django key-value store  

It can be useful for storing key-value pairs from a client in scenarios in which a relational database structure is not needed or is too heavy-weight.

An example usage would be to store settings in an ajax application about whether or not a user has left a modal window minimized.

Usage
--
POST to /store/ with key-value pairs. Many key/value pairs can be passed, and existing keys can be overriden.  

GET to /retrieve/ to retrieve a JSON object of key-value pairs. GET parameters should be a list of keys to retrieve. Only keys that exist will appear in the JSON.  

Keys are sandboxed to the logged in user (the user must be logged in to store or retrieve keys), so multiple users can use the same keys without collision.  

See tests.py for an example.  

Installation:
--
1) Add "js\_store" to your INSTALLED\_APPS  
2) Run syncdb  
