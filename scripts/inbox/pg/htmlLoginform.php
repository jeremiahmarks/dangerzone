<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 16:11:53
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 21:37:38
 */
function loginForm(){
    ?>
    <div class="loginForm">
        <form id="login" name="login" method='POST' action=''>
            <div class="loginFormFields">
                <span class="loginHeader">Login!</span>
                <div class="loginUsername">
                    <input type="text" name="username">
                </div>
                <div class="loginPassword">
                    <input type="password" name="password">
                </div>
                <div class="loginSubmit">
                    <input type="submit" name="login" value="login">
                </div>
            </div>
        </form>
    </div>
    <?php
}