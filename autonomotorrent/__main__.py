"""
"""
from twisted.python import log
from BTApp import BTApp, BTConfig
#from . import __version__ as VERSION

__version__ = "0.5.1"
VERSION=__version__

def main(opt, btfiles):
    app = BTApp(save_dir=opt.save_dir,
                listen_port=opt.listen_port,
                enable_DHT=opt.enable_dht,
                remote_debugging=opt.remote_debugging)
    for torrent_file in btfiles:
        try:
            log.msg('Adding: {0}'.format(torrent_file))
            config = BTConfig(torrent_file)
            config.downloadList = None
            app.add_torrent(config)

        except:
            log.err()
            log.err("Failed to add {0}".format(torrent_file))

    app.start_reactor()


def console():
    print("AutonomoTorrent v{0}".format(VERSION))
    from optparse import OptionParser

    usage = 'usage: %prog [options] torrent1 torrent2 ...'
    parser = OptionParser(usage=usage)
    parser.add_option('-o', '--output_dir', action='store', type='string',
                      dest='save_dir', default='.',
                      help='save download file to which directory')
    parser.add_option('-l', '--listen-port', action='store', type='int',
                      dest='listen_port', default=6881,
                      help='Bittorrent listen port')
    parser.add_option("-d", "--enable_dht", action="store_true",
                      dest="enable_dht", help="enable the DHT extension")
    parser.add_option("--remote_debug", action="store_true",
                      dest="remote_debugging",
                      help="enable remote debugging through twisted's manhole" + \
                           " telnet service on port 9999 (username & password: admin)")

    options, args = parser.parse_args()
    if (len(args) > 0):
        main(options, args)
    else:
        print("Error: No torrent files given.")
        print(usage)


if __name__ == '__main__':
    console()
