import DataDisplay as dd
import IMDBRequest as req
import sys

def main(argv):
    for arg in argv:
        if arg == 'reload':
            req.make_request()

    dd.plot_scores()

if __name__ == "__main__":
    main(sys.argv[1:])
