<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-21 21:11:31
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-21 21:40:55
 */
include_once 'functions.php';
/*
since this will interact with posts, a collection of return statuses would be nice.
100 => 'Continue',
101 => 'Switching Protocols',
102 => 'Processing',
200 => 'OK',
201 => 'Created',
202 => 'Accepted',
203 => 'Non-Authoritative Information',
204 => 'No Content',
205 => 'Reset Content',
206 => 'Partial Content',
207 => 'Multi-Status',
300 => 'Multiple Choices',
301 => 'Moved Permanently',
302 => 'Found',
303 => 'See Other',
304 => 'Not Modified',
305 => 'Use Proxy',
307 => 'Temporary Redirect',
400 => 'Bad Request',
401 => 'Unauthorized',
402 => 'Payment Required',
403 => 'Forbidden',
404 => 'Not Found',
405 => 'Method Not Allowed',
406 => 'Not Acceptable',
407 => 'Proxy Authentication Required',
408 => 'Request Timeout',
409 => 'Conflict',
410 => 'Gone',
411 => 'Length Required',
412 => 'Precondition Failed',
413 => 'Request Entity Too Large',
414 => 'Request-URI Too Long',
415 => 'Unsupported Media Type',
416 => 'Requested Range Not Satisfiable',
417 => 'Expectation Failed',
422 => 'Unprocessable Entity',
423 => 'Locked',
424 => 'Failed Dependency',
426 => 'Upgrade Required',
500 => 'Internal Server Error',
501 => 'Not Implemented',
502 => 'Bad Gateway',
503 => 'Service Unavailable',
504 => 'Gateway Timeout',
505 => 'HTTP Version Not Supported',
506 => 'Variant Also Negotiates',
507 => 'Insufficient Storage',
509 => 'Bandwidth Limit Exceeded',
510 => 'Not Extended'


*/
if (isset($_POST['preset'])){
    presets($_POST['preset']);
    return header($_SERVER['SERVER_PROTOCOL'] . '200 OK', true, 200);

} else {
    return header($_SERVER['SERVER_PROTOCOL'] . '501 Not Implemented', true, 501);
}
