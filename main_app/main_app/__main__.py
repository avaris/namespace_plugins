import importlib
import pkgutil

import main_app.plugins


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

def main():
    plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(main_app.plugins)
    }

    if plugins:
        print('Plugins found:')
        for name, plugin in plugins.items():
            print('\t{:30s} : {}'.format(name, plugin.NAME))
    else:
        print('No plugins are installed')


if __name__ == '__main__':
    main()