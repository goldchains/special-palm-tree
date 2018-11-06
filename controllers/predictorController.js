'use strict';
import {PythonShell} from 'python-shell';

export function predict_test1(req, res){
    console.log("predictor1")
    PythonShell.run('./ClassData/temp.py', {args: [req.params.course, req.params.test1]}, function (err, results){
    if(err){
        console.log(err);
        return res.json({errorType:'PythonShell', errorMessage: err})
    }
    res.json(results);
    });
};

export function predict_test2(req, res) {
    console.log("predictor2")
    PythonShell.run('./ClassData/temp.py', {args: [req.params.course, req.params.test1, req.params.test2]}, function (err, results){
        if(err){
            console.log(err);
            return res.json({errorType:'PythonShell', errorMessage: err})
        }
        res.json(results)
    });
};