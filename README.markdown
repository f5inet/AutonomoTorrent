##About
This is a fork of [ABTorrent](http://code.google.com/p/abtorrent/) which is a
pure Python implementation of a minimal BitTorrent client. The name 
AutonomoTorrent is short for Autonomous Torrent.  Autonomous in this context 
[means](http://www.merriam-webster.com/dictionary/autonomous) "existing or
capable of existing independently," which refers to its pure Python nature.  
    
Autonomo came about because I wanted to use BitTorrent in another Python
project of mine ([AdroitGM](https://github.com/joshsziegler/AdroitGM)), but 
found that most of the well-known Python clients relied upon
[Rasterbar's libtorrent](http://www.rasterbar.com/products/libtorrent/) which
is in C.  This worked well for dedicated clients, but all I wanted was a
no-frills, good-enough client to integrate into another application for
distributed file sharing.  I looked at serveral pure-Python projects before
settling on ABTorrent due to its minimal featureset and relatively 
up-to-date codebase (have a look at the old "Mainline" client code to get an 
idea of what I was comparing it against).  
  
Please keep in mind that this will remain a minimal, pure python client.  I 
have put it on GitHub for easier forking for those with more grandiose 
desires.  I *will* happily accept pull requests or patches for bugs however.  

##License 
As the original ABTorrent, this is released under the
[GPLv3](http://www.gnu.org/licenses/gpl.html).

##Install

```
git clone git://github.com/joshsziegler/AutonomoTorrent.git  
cd AutonomoTorrent  
sudo python setup.py install  
autonomo ~/torrents/damn_small_linux.torrent  
```

If you have issues with Twisted while running setup, first make sure you have
the python dev stuff installed (`sudo apt-get install python-dev build-essential` 
on Ubuntu).  If that doesn't work, you might be better off simply installing it 
manually.  
  
  - Ubuntu: `sudo apt-get install python-twisted`  
  - Windows: Get the [installer here](http://twistedmatrix.com/trac/wiki/Downloads#Windows).  

##Development
Develpoment is slow to non-existent at the moment as real life has caught up
with me.  If you want to help though, the biggest need is to refactor 
the code base as it is mostly unchanged from the original ABTorrent, and is 
really ugly in places.  The next biggest issue would be to write unit tests for
everything.

Either way, when submitting patches or pull requests, please at least run your
code though pylint and the cylomatic complexity tests bundled with the
test/pre-commit script. You don't have to fix everything, but at least attempt
to stick to PEP 8 and keep your CC under 8.

```
cd AutonomoTorrent
tests/pre-commit
```

 ##TestEdit
 Loren ipsum dolor sit amet.
 
