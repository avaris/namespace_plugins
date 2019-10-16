# Testing namespace plugins and discovery


```shell
(namespace_testing) ~/workspace/namespace_test  ls
main_app  plugin1  plugin2

(namespace_testing) ~/workspace/namespace_test  pip install -q main_app/

(namespace_testing) ~/workspace/namespace_test  main_app
No plugins are installed

(namespace_testing) ~/workspace/namespace_test  pip install -q plugin1/

(namespace_testing) ~/workspace/namespace_test  main_app
Plugins found:
        main_app.plugins.plugin1       : plugin1

(namespace_testing) ~/workspace/namespace_test  pip install -q plugin2/

(namespace_testing) ~/workspace/namespace_test  main_app
Plugins found:
        main_app.plugins.plugin1       : plugin1
        main_app.plugins.plugin2       : plugin2

(namespace_testing) ~/workspace/namespace_test  pip list
Package          Version
---------------- -------
main-app         1.0
main-app-plugin1 1.0
main-app-plugin2 1.0
pip              19.3
setuptools       41.4.0
wheel            0.33.6

(namespace_testing) ~/workspace/namespace_test  pip uninstall -yq main-app-plugin1

(namespace_testing) ~/workspace/namespace_test  main_app
Plugins found:
        main_app.plugins.plugin2       : plugin2
```