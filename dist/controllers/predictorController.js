'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.predict_test1 = predict_test1;
exports.predict_test2 = predict_test2;

var _pythonShell = require('python-shell');

function predict_test1(req, res) {
    console.log("predictor1");
    _pythonShell.PythonShell.run('./ClassData/temp.py', { args: [req.params.course, req.params.test1] }, function (err, results) {
        if (err) {
            console.log(err);
            return res.json({ errorType: 'PythonShell', errorMessage: err });
        }
        res.json(results);
    });
};

function predict_test2(req, res) {
    console.log("predictor2");
    _pythonShell.PythonShell.run('./ClassData/temp.py', { args: [req.params.course, req.params.test1, req.params.test2] }, function (err, results) {
        if (err) {
            console.log(err);
            return res.json({ errorType: 'PythonShell', errorMessage: err });
        }
        res.json(results);
    });
};