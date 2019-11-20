// Copyright (c) Jeremy Tuloup
// Distributed under the terms of the Modified BSD License.

import {
  JupyterFrontEndPlugin,
  JupyterFrontEnd,
  ILabShell
} from '@jupyterlab/application';

import { IJupyterWidgetRegistry } from '@jupyter-widgets/base';

import * as widgetExports from './widget';

import { MODULE_NAME, MODULE_VERSION } from './version';

const EXTENSION_ID = 'ipylab:plugin';

const extension: JupyterFrontEndPlugin<void> = {
  id: EXTENSION_ID,
  autoStart: true,
  requires: [IJupyterWidgetRegistry, ILabShell],
  activate: (
    app: JupyterFrontEnd,
    registry: IJupyterWidgetRegistry,
    shell: ILabShell
  ): void => {
    // add globals
    widgetExports.JupyterFrontEndModel._app = app;
    widgetExports.ShellModel._shell = shell;
    widgetExports.CommandRegistryModel._commands = app.commands;

    registry.registerWidget({
      name: MODULE_NAME,
      version: MODULE_VERSION,
      exports: widgetExports
    });
  }
};

export default extension;
