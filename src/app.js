// get html canvas element
var canvas = document.getElementById("canvas");

// create WebGL rendering context
var gl = canvas.getContext("webgl2");

// Check if browser supports WebGL
if (!gl) {
    alert("Your browser does not support WebGl");
}

// temp
gl.clearColor(0, 0.6, 0.0, 1.0);
gl.clear(gl.COLOR_BUFFER_BIT);

// WebGl Program
var program = gl.createProgram();

gl.linkProgram(program);
