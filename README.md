stagepatch
=======
Persistent JACK audio/MIDI and ALSA MIDI patchbay for [non session manager](http://non.tuxfamily.org/nsm/)
Unlike ````jackpatch```` which comes with NSM, stagepatch does not auto-save connections when the session is saved. Sessions are only saved when manually saved through the GUI. This is to ensure that connections never get accidentally overwritten after they are set.

When stagepatch is opened by the session manager, it restores previously saved connections and continues to watch for new clients, and connects them when they appear.

Based on aj-snapshot

Thanks to @rhetr for writing the initial NSM code this is built on:
https://github.com/rhetr/nsm-git


Requirements
------------
* Python 3
* aj-snapshot
* liblo and pyliblo
* rofi for GUI
* Non Session Manager
