<?php
$jscode=file_get_contents("en.js");
preg_match_all("/b\('[^']*'[\s]*,[\s]*'[^']*'\)/i", $jscode, $res);
if(isset($res))
{
 $res[0]=array_values(array_unique ($res[0]));
 ksort($res[0]);
 usort($res[0],function($a,$b){return strlen($b)-strlen($a);});
 $JS =file_get_contents("decoded.js");
 $v8 = new V8Js();
 try 
 {
 $v8->executeString($JS, 'basic.js');
 } catch (V8JsException $e) 
 {
 print_r($e);
    die();
 }
 foreach( $res[0] as $k => $v){
 preg_match_all("/'([^']*)'[\s]*,[\s]*'([^']*)'/i", $v, $res1);
 $JS='b("'.$res1[1][0].'", "'. $res1[2][0] .'");';
 $vv = $v8->executeString($JS, 'basic.js');
 $jscode=str_ireplace(array('window['.$v.']',$v),array($vv,"'".$vv."'"),$jscode);
 }
}
echo "ok!";
file_put_contents("src.js",$jscode);
die();





