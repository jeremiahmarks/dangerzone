<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 14:46:28
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 21:39:23
 */
function newUserForm(){
    ?>
    <div class="newUserForm">
        <form id="newUser" name="newUser" method='POST' action=''>
            <div class="newUserFormFields">
                <span class="newuserHeader">New User</span>
                <div class="newUserUsername">
                    <input type="text" name="username">
                </div>
                <div class="newUserPassword">
                    <input type="password" name="password">
                </div>
                <div class="newUserSubmit">
                    <input type="submit" name="createUser" value="Create Account">
                </div>
            </div>
        </form>
    </div>
    <?php
}