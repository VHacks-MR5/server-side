'use strict'; /**
               * Copyright (c) 2014, Facebook, Inc. All rights reserved.
               *
               * This source code is licensed under the BSD-style license found in the
               * LICENSE file in the root directory of this source tree. An additional grant
               * of patent rights can be found in the PATENTS file in the same directory.
               *
               * 
               */

var chalk = require('chalk');

exports.NO_DIFF_MESSAGE = chalk.dim(
'Compared values have no visual difference.');


exports.SIMILAR_MESSAGE = chalk.dim(
'Compared values serialize to the same structure.\n' +
'Printing internal object structure without calling `toJSON` instead.');