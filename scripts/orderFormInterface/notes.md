from https://if188.infusionsoft.com/app/manageCart/addProduct?productId=127
<form id="checkout" name="checkout" method="post" action="/app/manageCart/updateCart">
                    <input type="hidden" value="false" name="proceedToCheckout" id="proceedToCheckout">
                    <input type="hidden" value="" name="purchasableProductIds" id="purchasableProductIds">
                    <input type="hidden" value="" name="quantities" id="quantities">
                    <input type="hidden" value="" name="removePurchasableProductId" id="removePurchasableProductId">
                    <input type="hidden" value="" name="upSellId" id="upSellId">
                    <div id="header">
                        <div id="CUSTOM_HTML">
                            <div id="customHeader">
                            </div>
                        </div>
                    <div id="IMAGE">
                        <div id="companyLogoTopBanner">
        <img src="https://d1yoaun8syyxxt.cloudfront.net/if188-dd91732f-2302-446b-9763-d30d6fe1a96a-v2">
    </div>    </div>                        </div>
                        <div id="contentWide">
    <div id="CHECKOUT_LINKS_TOP"><link type="text/css" rel="stylesheet" href="/css/anti_spam.jsp?b=1.40.0.41"><script type="text/javascript">(function() {
                        var styleArray = ["/css/anti_spam.jsp"];
                        if (window.Infusion) {
                            Infusion.stylesLoaded(styleArray);
                        } else if (window.InfusionStyles) {
                            window.InfusionStyles.concat(styleArray);
                        } else {
                            window.InfusionStyles = styleArray;
                        }                    })();</script><div class="checkoutLinksTop">
    <input type="hidden" value="true" name="version3state" id="version3state">
        <a class="continueButton" href="/app/storeFront/showStoreFront">Continue Shopping</a>
</div>    </div>
    <div id="CUSTOM_HTML">
<div id="customCheckoutTop">
    Guests Name <input type="text" name="Contact0_GuestsName" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABHklEQVQ4EaVTO26DQBD1ohQWaS2lg9JybZ+AK7hNwx2oIoVf4UPQ0Lj1FdKktevIpel8AKNUkDcWMxpgSaIEaTVv3sx7uztiTdu2s/98DywOw3Dued4Who/M2aIx5lZV1aEsy0+qiwHELyi+Ytl0PQ69SxAxkWIA4RMRTdNsKE59juMcuZd6xIAFeZ6fGCdJ8kY4y7KAuTRNGd7jyEBXsdOPE3a0QGPsniOnnYMO67LgSQN9T41F2QGrQRRFCwyzoIF2qyBuKKbcOgPXdVeY9rMWgNsjf9ccYesJhk3f5dYT1HX9gR0LLQR30TnjkUEcx2uIuS4RnI+aj6sJR0AM8AaumPaM/rRehyWhXqbFAA9kh3/8/NvHxAYGAsZ/il8IalkCLBfNVAAAAABJRU5ErkJggg==&quot;); background-repeat: no-repeat; background-attachment: scroll; background-position: right center;">  <br>
Dietary Concerns:  <textarea name="Contact0_DietaryRestrictions" cols="50" rows="4"></textarea>
</div>
    </div>
    <div id="PAYMENT_PLANS">        <table class="payPlan tabular grid">                <tbody><tr>
                    <th class="leftAlign">Payment Plans</th>
                    <th></th>
                </tr>            <tr>
                <td>
                    <input type="radio" checked="" value="0" name="payPlanId" class="choosePlan" onclick="Infusion.ManageCart.ajaxSubmitForm(jQuery('.payPlan').closest('form').attr('id'), false, 0, 0,['BRIEF_PRODUCT_SUMMARY', 'BILLING_ENTRY', 'SHIPPING_ENTRY', 'PAYMENT_SELECTION', 'CHECKOUT_LINKS_TOP', 'CHECKOUT_LINKS']);">
                        Single payment of
                </td>
                <td class="rightAlign">$133.00</td>
            </tr>                <tr>
                    <td>
                        <input type="radio" value="3" name="payPlanId" class="choosePlan" onclick="Infusion.ManageCart.ajaxSubmitForm(jQuery('.payPlan').closest('form').attr('id'), false, 0, 0,['BRIEF_PRODUCT_SUMMARY', 'BILLING_ENTRY', 'SHIPPING_ENTRY', 'PAYMENT_SELECTION', 'CHECKOUT_LINKS_TOP', 'CHECKOUT_LINKS']);">
                            3&nbsp;payments of
                            <p class="financeCharge">(Finance Charge $300.00)</p>
                    </td>
                    <td class="rightAlign">$144.33</td>
                </tr>
        </tbody></table>    </div>
    <div id="BRIEF_PRODUCT_SUMMARY">    <h1>Shopping Cart</h1>
<input type="hidden" value="false" name="isShippingRequired" id="isShippingRequired">
<input type="hidden" value="false" name="isCartEmpty" id="isCartEmpty"><div class="tableContainer">
    <table class="viewCart tabular grid">
        <tbody><tr>
            <th colspan="2" class="leftAlign">Name</th>
            <th class="rightAlign">Price</th>
            <th class="centerAlign">Qty</th>
            <th class="rightAlign">Total</th>
        </tr>
                    <tr>
                                <td colspan="2" class="leftAlign">                            <p class="cartProduct">membershipSite</p>
                            <p class="cartDescription"> </p>
                                <a href="javascript:Infusion.ManageCart.ajaxSubmitForm(jQuery('.viewCart').closest('form').attr('id'), false, '1', 0, ['BRIEF_PRODUCT_SUMMARY','UP_SELLS','PAYMENT_PLANS','SHIPPING_OPTIONS', 'SHIPPING_ENTRY', 'BILLING_ENTRY','PAYMENT_SELECTION','CHECKOUT_LINKS','CHECKOUT_LINKS_TOP']);">Remove</a>
                        </td>
                        <td class="rightAlign">
                                    <span class="price">$133.00</span>
                        </td>
                        <td class="centerAlign">
                                    <input type="text" size="1" value="1" name="qty_1" class="qtyField">
                                    <a class="updateCart" href="javascript:Infusion.ManageCart.ajaxSubmitForm(jQuery('.viewCart').closest('form').attr('id'), false, 0, 0, ['BRIEF_PRODUCT_SUMMARY','UP_SELLS','PAYMENT_PLANS', 'SHIPPING_OPTIONS', 'SHIPPING_ENTRY', 'BILLING_ENTRY','PAYMENT_SELECTION','CHECKOUT_LINKS','CHECKOUT_LINKS_TOP']);">Update</a>
                        </td>
                        <td class="rightAlign">
                            $133.00
                        </td>
                    </tr>
        <tr class="subtotal">
            <td colspan="2" class="leftAlign">Sub Total:</td>
            <td class="rightAlign"></td>
            <td class="centerAlign"></td>
            <td class="rightAlign">$133.00</td>
        </tr>
    </tbody></table>
</div>    </div>
    <div id="PROMO_CODE">    <table class="promoCode">
        <tbody><tr>
            <td align="left">
                    Enter a Promo Code:
            </td>
            <td>
                <input type="text" name="promoCode" id="promoCode" class="promoField">
                <a class="codeButton" href="javascript:Infusion.ManageCart.ajaxSubmitForm('checkout', false, 0, 0, ['BRIEF_PRODUCT_SUMMARY','PAYMENT_PLANS', 'PROMO_CODE', 'UP_SELLS']);">Apply</a>
            </td>
        </tr>
    </tbody></table>    </div>
    <div id="UP_SELLS">    </div>
    <div id="BILLING_ENTRY">
<table class="billingTable tabular grid">
        <tbody><tr>
            <th align="left" colspan="2">Billing Information</th>
        </tr>
    <tr>
        <td class="rightAlignTop"><label class="checkoutLabel">* First Name</label></td>
        <td>
                    <input type="text" size="10" name="firstName" id="firstName" data-constraints="@Required(label=&quot;First Name&quot;, groups=[customer])" class="regula-validation checkoutTop">
                    <input type="text" name="inf_95O2gIEAKtVu6WBV" id="inf_95O2gIEAKtVu6WBV" class="inf_a793efe1f52b80b9050125021f2cfb6a">
        </td>
    </tr>
    <tr>
        <td class="rightAlign"><label class="checkoutLabel">* Last Name</label></td>
        <td>
                    <input type="text" size="12" name="lastName" id="lastName" data-constraints="@Required(label=&quot;Last Name&quot;, groups=[customer])" class="regula-validation checkout">
        </td>
    </tr>
    <tr>
        <td class="rightAlign">
            <label class="checkoutLabel">
                        Company Name
            </label>
        </td>
        <td>
                            <input type="text" size="25" name="company" id="company" class="checkout">
        </td>
    </tr>
    <tr>
        <td class="rightAlign"><label class="checkoutLabel">* Address - Line 1</label></td>
        <td><input type="text" size="25" name="addressLine1" id="addressLine1" data-constraints="@Required(label=&quot;Address - Line 1&quot;, groups=[customer])" class="regula-validation checkout"></td>
    </tr>
    <tr>
        <td class="rightAlign"><label class="checkoutLabel">Address - Line 2</label></td>
        <td><input type="text" size="25" name="addressLine2" id="addressLine2" class="checkout"></td>
    </tr>
    <tr>
        <td class="rightAlign"><label class="checkoutLabel">* City</label></td>
        <td><input type="text" size="15" name="city" id="city" data-constraints="@Required(label=&quot;City&quot;, groups=[customer])" class="regula-validation checkout"></td>
    </tr>
    <tr>
        <td class="rightAlign"><label class="checkoutLabel"><div id="stateRequired">* State</div></label></td>
        <td>
                    <input type="text" size="2" name="state" id="state" data-constraints="@StateRequiredForSpecificCountries(countryFieldName=&quot;country&quot;, label=&quot;State&quot;, groups=[customer])" class="regula-validation checkout">
        </td>
    </tr>
    <tr>
        <td class="rightAlign"><label class="checkoutLabel">* Zip Code</label></td>
        <td><input type="text" size="5" name="zipCode" id="zipCode" data-constraints="@Required(label=&quot;Zip Code&quot;, groups=[customer])" class="regula-validation checkoutShort"></td>
    </tr>
            <tr>
                <td class="rightAlign"><label class="checkoutLabel">* Country</label></td>
                <td><select data-on="Component.Select" name="country" id="country" data-constraints="@Required(label=&quot;Billing Country&quot;, groups=[customer])" class="regula-validation checkoutShort"><option value="">Please select one</option><option value="Afghanistan">Afghanistan</option><option value="Albania">Albania</option><option value="Algeria">Algeria</option><option value="American Samoa">American Samoa</option><option value="Andorra">Andorra</option><option value="Angola">Angola</option><option value="Anguilla">Anguilla</option><option value="Antarctica">Antarctica</option><option value="Antigua and Barbuda">Antigua and Barbuda</option><option value="Argentina">Argentina</option><option value="Armenia">Armenia</option><option value="Aruba">Aruba</option><option value="Australia">Australia</option><option value="Austria">Austria</option><option value="Åland Islands">Åland Islands</option><option value="Azerbaijan">Azerbaijan</option><option value="Bahamas">Bahamas</option><option value="Bahrain">Bahrain</option><option value="Bangladesh">Bangladesh</option><option value="Barbados">Barbados</option><option value="Belarus">Belarus</option><option value="Belgium">Belgium</option><option value="Belize">Belize</option><option value="Benin">Benin</option><option value="Bermuda">Bermuda</option><option value="Bhutan">Bhutan</option><option value="Bolivia">Bolivia</option><option value="Bosnia and Herzegovina">Bosnia and Herzegovina</option><option value="Botswana">Botswana</option><option value="Bouvet Island">Bouvet Island</option><option value="Brazil">Brazil</option><option value="British Indian Ocean Territory">British Indian Ocean Territory</option><option value="Brunei Darussalam">Brunei Darussalam</option><option value="Bulgaria">Bulgaria</option><option value="Burkina Faso">Burkina Faso</option><option value="Burundi">Burundi</option><option value="Cambodia">Cambodia</option><option value="Cameroon">Cameroon</option><option value="Canada">Canada</option><option value="Cape Verde">Cape Verde</option><option value="Cayman Islands">Cayman Islands</option><option value="Central African Republic">Central African Republic</option><option value="Chad">Chad</option><option value="Chile">Chile</option><option value="China">China</option><option value="Christmas Island">Christmas Island</option><option value="Cocos (Keeling) Islands">Cocos (Keeling) Islands</option><option value="Colombia">Colombia</option><option value="Comoros">Comoros</option><option value="Congo">Congo</option><option value="Democratic Republic Of Congo">Democratic Republic Of Congo</option><option value="Cook Islands">Cook Islands</option><option value="Costa Rica">Costa Rica</option><option value="Croatia">Croatia</option><option value="Cuba">Cuba</option><option value="Cyprus">Cyprus</option><option value="Czech Republic">Czech Republic</option><option value="Côte D'Ivoire">Côte D'Ivoire</option><option value="Denmark">Denmark</option><option value="Djibouti">Djibouti</option><option value="Dominica">Dominica</option><option value="Dominican Republic">Dominican Republic</option><option value="Ecuador">Ecuador</option><option value="Egypt">Egypt</option><option value="El Salvador">El Salvador</option><option value="Equatorial Guinea">Equatorial Guinea</option><option value="Eritrea">Eritrea</option><option value="Estonia">Estonia</option><option value="Ethiopia">Ethiopia</option><option value="Falkland Islands">Falkland Islands</option><option value="Faroe Islands">Faroe Islands</option><option value="Fiji">Fiji</option><option value="Finland">Finland</option><option value="France">France</option><option value="French Guiana">French Guiana</option><option value="French Polynesia">French Polynesia</option><option value="French Southern Territories">French Southern Territories</option><option value="Gabon">Gabon</option><option value="Gambia">Gambia</option><option value="Georgia">Georgia</option><option value="Germany">Germany</option><option value="Ghana">Ghana</option><option value="Gibraltar">Gibraltar</option><option value="Greece">Greece</option><option value="Greenland">Greenland</option><option value="Grenada">Grenada</option><option value="Guadeloupe">Guadeloupe</option><option value="Guam">Guam</option><option value="Guatemala">Guatemala</option><option value="Guernsey">Guernsey</option><option value="Guinea">Guinea</option><option value="Guinea-Bissau">Guinea-Bissau</option><option value="Guyana">Guyana</option><option value="Haiti">Haiti</option><option value="Heard and McDonald Islands">Heard and McDonald Islands</option><option value="Holy See (Vatican City State)">Holy See (Vatican City State)</option><option value="Honduras">Honduras</option><option value="Hong Kong">Hong Kong</option><option value="Hungary">Hungary</option><option value="Iceland">Iceland</option><option value="India">India</option><option value="Indonesia">Indonesia</option><option value="Iran">Iran</option><option value="Iraq">Iraq</option><option value="Ireland">Ireland</option><option value="Isle of Man">Isle of Man</option><option value="Israel">Israel</option><option value="Italy">Italy</option><option value="Jamaica">Jamaica</option><option value="Japan">Japan</option><option value="Jersey">Jersey</option><option value="Jordan">Jordan</option><option value="Kazakhstan">Kazakhstan</option><option value="Kenya">Kenya</option><option value="Kiribati">Kiribati</option><option value="North Korea">North Korea</option><option value="South Korea">South Korea</option><option value="Kuwait">Kuwait</option><option value="Kyrgyzstan">Kyrgyzstan</option><option value="Laos">Laos</option><option value="Latvia">Latvia</option><option value="Lebanon">Lebanon</option><option value="Lesotho">Lesotho</option><option value="Liberia">Liberia</option><option value="Libya">Libya</option><option value="Liechtenstein">Liechtenstein</option><option value="Lithuania">Lithuania</option><option value="Luxembourg">Luxembourg</option><option value="Macao">Macao</option><option value="Republic of Macedonia">Republic of Macedonia</option><option value="Madagascar">Madagascar</option><option value="Malawi">Malawi</option><option value="Malaysia">Malaysia</option><option value="Maldives">Maldives</option><option value="Mali">Mali</option><option value="Malta">Malta</option><option value="Marshall Islands">Marshall Islands</option><option value="Martinique">Martinique</option><option value="Mauritania">Mauritania</option><option value="Mauritius">Mauritius</option><option value="Mayotte">Mayotte</option><option value="Mexico">Mexico</option><option value="Federated States of Micronesia">Federated States of Micronesia</option><option value="Moldova">Moldova</option><option value="Monaco">Monaco</option><option value="Mongolia">Mongolia</option><option value="Montenegro">Montenegro</option><option value="Montserrat">Montserrat</option><option value="Morocco">Morocco</option><option value="Mozambique">Mozambique</option><option value="Myanmar">Myanmar</option><option value="Namibia">Namibia</option><option value="Nauru">Nauru</option><option value="Nepal">Nepal</option><option value="Netherlands">Netherlands</option><option value="Netherlands Antilles">Netherlands Antilles</option><option value="New Caledonia">New Caledonia</option><option value="New Zealand">New Zealand</option><option value="Nicaragua">Nicaragua</option><option value="Niger">Niger</option><option value="Nigeria">Nigeria</option><option value="Niue">Niue</option><option value="Norfolk Island">Norfolk Island</option><option value="Northern Mariana Islands">Northern Mariana Islands</option><option value="Norway">Norway</option><option value="Oman">Oman</option><option value="Pakistan">Pakistan</option><option value="Palau">Palau</option><option value="Palestine">Palestine</option><option value="Panama">Panama</option><option value="Papua New Guinea">Papua New Guinea</option><option value="Paraguay">Paraguay</option><option value="Peru">Peru</option><option value="Philippines">Philippines</option><option value="Pitcairn">Pitcairn</option><option value="Poland">Poland</option><option value="Portugal">Portugal</option><option value="Puerto Rico">Puerto Rico</option><option value="Qatar">Qatar</option><option value="Romania">Romania</option><option value="Russian Federation">Russian Federation</option><option value="Rwanda">Rwanda</option><option value="Réunion">Réunion</option><option value="St. Barthélemy">St. Barthélemy</option><option value="St. Helena, Ascension and Tristan Da Cunha">St. Helena, Ascension and Tristan Da Cunha</option><option value="St. Kitts And Nevis">St. Kitts And Nevis</option><option value="St. Lucia">St. Lucia</option><option value="St. Martin">St. Martin</option><option value="St. Pierre And Miquelon">St. Pierre And Miquelon</option><option value="St. Vincent And The Grenedines">St. Vincent And The Grenedines</option><option value="Samoa">Samoa</option><option value="San Marino">San Marino</option><option value="Sao Tome and Principe">Sao Tome and Principe</option><option value="Saudi Arabia">Saudi Arabia</option><option value="Senegal">Senegal</option><option value="Serbia">Serbia</option><option value="Seychelles">Seychelles</option><option value="Sierra Leone">Sierra Leone</option><option value="Singapore">Singapore</option><option value="Slovakia">Slovakia</option><option value="Slovenia">Slovenia</option><option value="Solomon Islands">Solomon Islands</option><option value="Somalia">Somalia</option><option value="South Africa">South Africa</option><option value="South Georgia and the South Sandwich Islands">South Georgia and the South Sandwich Islands</option><option value="Spain">Spain</option><option value="Sri Lanka">Sri Lanka</option><option value="Sudan">Sudan</option><option value="Suriname">Suriname</option><option value="Svalbard And Jan Mayen">Svalbard And Jan Mayen</option><option value="Swaziland">Swaziland</option><option value="Sweden">Sweden</option><option value="Switzerland">Switzerland</option><option value="Syrian Arab Republic">Syrian Arab Republic</option><option value="Taiwan">Taiwan</option><option value="Tajikistan">Tajikistan</option><option value="Tanzania">Tanzania</option><option value="Thailand">Thailand</option><option value="Timor-Leste">Timor-Leste</option><option value="Togo">Togo</option><option value="Tokelau">Tokelau</option><option value="Tonga">Tonga</option><option value="Trinidad and Tobago">Trinidad and Tobago</option><option value="Tunisia">Tunisia</option><option value="Turkey">Turkey</option><option value="Turkmenistan">Turkmenistan</option><option value="Turks and Caicos Islands">Turks and Caicos Islands</option><option value="Tuvalu">Tuvalu</option><option value="Uganda">Uganda</option><option value="Ukraine">Ukraine</option><option value="United Arab Emirates">United Arab Emirates</option><option value="United Kingdom">United Kingdom</option><option value="United States" selected="selected">United States</option><option value="US Minor Outlying Islands">US Minor Outlying Islands</option><option value="Uruguay">Uruguay</option><option value="Uzbekistan">Uzbekistan</option><option value="Vanuatu">Vanuatu</option><option value="Venezuela">Venezuela</option><option value="Viet Nam">Viet Nam</option><option value="Virgin Islands, British">Virgin Islands, British</option><option value="Virgin Islands, U.S.">Virgin Islands, U.S.</option><option value="Wallis and Futuna">Wallis and Futuna</option><option value="Western Sahara">Western Sahara</option><option value="Yemen">Yemen</option><option value="Zambia">Zambia</option><option value="Zimbabwe">Zimbabwe</option></select></td>
            </tr>
    <tr>
        <td class="rightAlign">* Phone Number</td>
        <td><input type="text" size="25" name="phoneNumber" id="phoneNumber" data-constraints="@Required(label=&quot;Phone Number&quot;, groups=[customer])" class="regula-validation checkout"></td>
    </tr>
    <tr>
        <td class="rightAlign">* Email Address</td>
        <td><input type="text" size="15" name="emailAddress" id="emailAddress" data-constraints="@Required(label=&quot;Email Address&quot;, groups=[customer]) @Email(label=&quot;Email Address&quot;, groups=[customer])" class="regula-validation checkoutBottom"></td>
    </tr>
            <tr class="shippingCheckbox">
                <td class="" colspan="2">
                    <p class="addressTableInfo">
                        <input type="checkbox" onclick="Infusion.ManageCart.copyShipping(this, 'checkout', 'onestep', 'State', false)"> Shipping is the same as billing
                    </p>
                </td>
            </tr>
</tbody></table>
    <script type="text/javascript">jQuery('.billingTable').removeAttr('style');</script>
<script type="text/javascript">Infusion.on("ManageCart").readyExec(function() {    var $country = jQuery('#country');        if ($country.val() == 'United States' || $country.val() == 'Canada') {
            jQuery('#stateRequired').html('* State');
        }    if ($country.length &gt; 0 &amp;&amp; "SELECT" == $country.get(0).tagName) {
        $country.change(function() {            if ($country.val() == 'United States' || $country.val() == 'Canada') {
                jQuery('#stateRequired').html('* State');
            } else {
                jQuery('#stateRequired').html('State');
            }
        });    }    var formName = 'checkout';
    jQuery('#addressLine1, #city, #state, #zipCode, #country').bind('change', {formName: formName}, Infusion.ManageCart.taxAjaxCall);
        ;});</script>    </div>
    <div id="SHIPPING_ENTRY">    <table class="shippingTable tabular grid">
            <tbody><tr>
                <th align="left" colspan="2">Shipping Information</th>
            </tr>
        <tr>
            <td class="rightAlignTop"><label class="checkoutLabel">* First Name</label></td>
            <td><input type="text" size="10" name="shipFirstName" id="shipFirstName" data-constraints="@Required(label=&quot;Shipping First Name&quot;, groups=[customer])" class="regula-validation checkoutTop"></td>
        </tr>
        <tr>
            <td class="rightAlign"><label class="checkoutLabel">* Last Name</label></td>
            <td><input type="text" size="12" name="shipLastName" id="shipLastName" data-constraints="@Required(label=&quot;Shipping Last Name&quot;, groups=[customer])" class="regula-validation checkout"></td>
        </tr>
        <tr>
            <td class="rightAlign">
                <label class="checkoutLabel">
                            Company Name
                </label>
            </td>
            <td>
                                <input type="text" size="25" name="shipCompany" id="shipCompany" class="checkout">
            </td>
        </tr>
        <tr>
            <td class="rightAlign"><label class="checkoutLabel">* Address - Line 1</label></td>
            <td><input type="text" size="25" name="shipAddressLine1" id="shipAddressLine1" data-constraints="@Required(label=&quot;Shipping Address - Line 1&quot;, groups=[customer])" class="regula-validation checkout"></td>
        </tr>
        <tr>
            <td class="rightAlign"><label class="checkoutLabel">Address - Line 2</label></td>
            <td><input type="text" size="25" name="shipAddressLine2" id="shipAddressLine2" class="checkout"></td>
        </tr>
        <tr>
            <td class="rightAlign"><label class="checkoutLabel">* City</label></td>
            <td><input type="text" size="15" name="shipCity" id="shipCity" data-constraints="@Required(label=&quot;Shipping City&quot;, groups=[customer])" class="regula-validation checkout"></td>
        </tr>
        <tr>
            <td class="rightAlign"><label class="checkoutLabel"><div id="shippingStateRequired">* State</div></label></td>
            <td>
                        <input type="text" size="2" name="shipState" id="shipState" data-constraints="@StateRequiredForSpecificCountries(countryFieldName=&quot;shipCountry&quot;, label=&quot;Shipping State&quot;, groups=[customer])" class="regula-validation checkout">
            </td>
        </tr>
        <tr>
            <td class="rightAlign"><label class="checkoutLabel">* Zip Code</label></td>
            <td><input type="text" size="5" name="shipZipCode" id="shipZipCode" data-constraints="@Required(label=&quot;Shipping Zip Code&quot;, groups=[customer])" class="regula-validation checkoutShort"></td>
        </tr>
                <tr>
                    <td class="rightAlign"><label class="checkoutLabel">* Country</label></td>
                    <td><select data-on="Component.Select" name="shipCountry" id="shipCountry" data-constraints="@Required(label=&quot;Shipping Country&quot;, groups=[customer])" class="regula-validation checkoutShort"><option value="">Please select one</option><option value="Afghanistan">Afghanistan</option><option value="Albania">Albania</option><option value="Algeria">Algeria</option><option value="American Samoa">American Samoa</option><option value="Andorra">Andorra</option><option value="Angola">Angola</option><option value="Anguilla">Anguilla</option><option value="Antarctica">Antarctica</option><option value="Antigua and Barbuda">Antigua and Barbuda</option><option value="Argentina">Argentina</option><option value="Armenia">Armenia</option><option value="Aruba">Aruba</option><option value="Australia">Australia</option><option value="Austria">Austria</option><option value="Åland Islands">Åland Islands</option><option value="Azerbaijan">Azerbaijan</option><option value="Bahamas">Bahamas</option><option value="Bahrain">Bahrain</option><option value="Bangladesh">Bangladesh</option><option value="Barbados">Barbados</option><option value="Belarus">Belarus</option><option value="Belgium">Belgium</option><option value="Belize">Belize</option><option value="Benin">Benin</option><option value="Bermuda">Bermuda</option><option value="Bhutan">Bhutan</option><option value="Bolivia">Bolivia</option><option value="Bosnia and Herzegovina">Bosnia and Herzegovina</option><option value="Botswana">Botswana</option><option value="Bouvet Island">Bouvet Island</option><option value="Brazil">Brazil</option><option value="British Indian Ocean Territory">British Indian Ocean Territory</option><option value="Brunei Darussalam">Brunei Darussalam</option><option value="Bulgaria">Bulgaria</option><option value="Burkina Faso">Burkina Faso</option><option value="Burundi">Burundi</option><option value="Cambodia">Cambodia</option><option value="Cameroon">Cameroon</option><option value="Canada">Canada</option><option value="Cape Verde">Cape Verde</option><option value="Cayman Islands">Cayman Islands</option><option value="Central African Republic">Central African Republic</option><option value="Chad">Chad</option><option value="Chile">Chile</option><option value="China">China</option><option value="Christmas Island">Christmas Island</option><option value="Cocos (Keeling) Islands">Cocos (Keeling) Islands</option><option value="Colombia">Colombia</option><option value="Comoros">Comoros</option><option value="Congo">Congo</option><option value="Democratic Republic Of Congo">Democratic Republic Of Congo</option><option value="Cook Islands">Cook Islands</option><option value="Costa Rica">Costa Rica</option><option value="Croatia">Croatia</option><option value="Cuba">Cuba</option><option value="Cyprus">Cyprus</option><option value="Czech Republic">Czech Republic</option><option value="Côte D'Ivoire">Côte D'Ivoire</option><option value="Denmark">Denmark</option><option value="Djibouti">Djibouti</option><option value="Dominica">Dominica</option><option value="Dominican Republic">Dominican Republic</option><option value="Ecuador">Ecuador</option><option value="Egypt">Egypt</option><option value="El Salvador">El Salvador</option><option value="Equatorial Guinea">Equatorial Guinea</option><option value="Eritrea">Eritrea</option><option value="Estonia">Estonia</option><option value="Ethiopia">Ethiopia</option><option value="Falkland Islands">Falkland Islands</option><option value="Faroe Islands">Faroe Islands</option><option value="Fiji">Fiji</option><option value="Finland">Finland</option><option value="France">France</option><option value="French Guiana">French Guiana</option><option value="French Polynesia">French Polynesia</option><option value="French Southern Territories">French Southern Territories</option><option value="Gabon">Gabon</option><option value="Gambia">Gambia</option><option value="Georgia">Georgia</option><option value="Germany">Germany</option><option value="Ghana">Ghana</option><option value="Gibraltar">Gibraltar</option><option value="Greece">Greece</option><option value="Greenland">Greenland</option><option value="Grenada">Grenada</option><option value="Guadeloupe">Guadeloupe</option><option value="Guam">Guam</option><option value="Guatemala">Guatemala</option><option value="Guernsey">Guernsey</option><option value="Guinea">Guinea</option><option value="Guinea-Bissau">Guinea-Bissau</option><option value="Guyana">Guyana</option><option value="Haiti">Haiti</option><option value="Heard and McDonald Islands">Heard and McDonald Islands</option><option value="Holy See (Vatican City State)">Holy See (Vatican City State)</option><option value="Honduras">Honduras</option><option value="Hong Kong">Hong Kong</option><option value="Hungary">Hungary</option><option value="Iceland">Iceland</option><option value="India">India</option><option value="Indonesia">Indonesia</option><option value="Iran">Iran</option><option value="Iraq">Iraq</option><option value="Ireland">Ireland</option><option value="Isle of Man">Isle of Man</option><option value="Israel">Israel</option><option value="Italy">Italy</option><option value="Jamaica">Jamaica</option><option value="Japan">Japan</option><option value="Jersey">Jersey</option><option value="Jordan">Jordan</option><option value="Kazakhstan">Kazakhstan</option><option value="Kenya">Kenya</option><option value="Kiribati">Kiribati</option><option value="North Korea">North Korea</option><option value="South Korea">South Korea</option><option value="Kuwait">Kuwait</option><option value="Kyrgyzstan">Kyrgyzstan</option><option value="Laos">Laos</option><option value="Latvia">Latvia</option><option value="Lebanon">Lebanon</option><option value="Lesotho">Lesotho</option><option value="Liberia">Liberia</option><option value="Libya">Libya</option><option value="Liechtenstein">Liechtenstein</option><option value="Lithuania">Lithuania</option><option value="Luxembourg">Luxembourg</option><option value="Macao">Macao</option><option value="Republic of Macedonia">Republic of Macedonia</option><option value="Madagascar">Madagascar</option><option value="Malawi">Malawi</option><option value="Malaysia">Malaysia</option><option value="Maldives">Maldives</option><option value="Mali">Mali</option><option value="Malta">Malta</option><option value="Marshall Islands">Marshall Islands</option><option value="Martinique">Martinique</option><option value="Mauritania">Mauritania</option><option value="Mauritius">Mauritius</option><option value="Mayotte">Mayotte</option><option value="Mexico">Mexico</option><option value="Federated States of Micronesia">Federated States of Micronesia</option><option value="Moldova">Moldova</option><option value="Monaco">Monaco</option><option value="Mongolia">Mongolia</option><option value="Montenegro">Montenegro</option><option value="Montserrat">Montserrat</option><option value="Morocco">Morocco</option><option value="Mozambique">Mozambique</option><option value="Myanmar">Myanmar</option><option value="Namibia">Namibia</option><option value="Nauru">Nauru</option><option value="Nepal">Nepal</option><option value="Netherlands">Netherlands</option><option value="Netherlands Antilles">Netherlands Antilles</option><option value="New Caledonia">New Caledonia</option><option value="New Zealand">New Zealand</option><option value="Nicaragua">Nicaragua</option><option value="Niger">Niger</option><option value="Nigeria">Nigeria</option><option value="Niue">Niue</option><option value="Norfolk Island">Norfolk Island</option><option value="Northern Mariana Islands">Northern Mariana Islands</option><option value="Norway">Norway</option><option value="Oman">Oman</option><option value="Pakistan">Pakistan</option><option value="Palau">Palau</option><option value="Palestine">Palestine</option><option value="Panama">Panama</option><option value="Papua New Guinea">Papua New Guinea</option><option value="Paraguay">Paraguay</option><option value="Peru">Peru</option><option value="Philippines">Philippines</option><option value="Pitcairn">Pitcairn</option><option value="Poland">Poland</option><option value="Portugal">Portugal</option><option value="Puerto Rico">Puerto Rico</option><option value="Qatar">Qatar</option><option value="Romania">Romania</option><option value="Russian Federation">Russian Federation</option><option value="Rwanda">Rwanda</option><option value="Réunion">Réunion</option><option value="St. Barthélemy">St. Barthélemy</option><option value="St. Helena, Ascension and Tristan Da Cunha">St. Helena, Ascension and Tristan Da Cunha</option><option value="St. Kitts And Nevis">St. Kitts And Nevis</option><option value="St. Lucia">St. Lucia</option><option value="St. Martin">St. Martin</option><option value="St. Pierre And Miquelon">St. Pierre And Miquelon</option><option value="St. Vincent And The Grenedines">St. Vincent And The Grenedines</option><option value="Samoa">Samoa</option><option value="San Marino">San Marino</option><option value="Sao Tome and Principe">Sao Tome and Principe</option><option value="Saudi Arabia">Saudi Arabia</option><option value="Senegal">Senegal</option><option value="Serbia">Serbia</option><option value="Seychelles">Seychelles</option><option value="Sierra Leone">Sierra Leone</option><option value="Singapore">Singapore</option><option value="Slovakia">Slovakia</option><option value="Slovenia">Slovenia</option><option value="Solomon Islands">Solomon Islands</option><option value="Somalia">Somalia</option><option value="South Africa">South Africa</option><option value="South Georgia and the South Sandwich Islands">South Georgia and the South Sandwich Islands</option><option value="Spain">Spain</option><option value="Sri Lanka">Sri Lanka</option><option value="Sudan">Sudan</option><option value="Suriname">Suriname</option><option value="Svalbard And Jan Mayen">Svalbard And Jan Mayen</option><option value="Swaziland">Swaziland</option><option value="Sweden">Sweden</option><option value="Switzerland">Switzerland</option><option value="Syrian Arab Republic">Syrian Arab Republic</option><option value="Taiwan">Taiwan</option><option value="Tajikistan">Tajikistan</option><option value="Tanzania">Tanzania</option><option value="Thailand">Thailand</option><option value="Timor-Leste">Timor-Leste</option><option value="Togo">Togo</option><option value="Tokelau">Tokelau</option><option value="Tonga">Tonga</option><option value="Trinidad and Tobago">Trinidad and Tobago</option><option value="Tunisia">Tunisia</option><option value="Turkey">Turkey</option><option value="Turkmenistan">Turkmenistan</option><option value="Turks and Caicos Islands">Turks and Caicos Islands</option><option value="Tuvalu">Tuvalu</option><option value="Uganda">Uganda</option><option value="Ukraine">Ukraine</option><option value="United Arab Emirates">United Arab Emirates</option><option value="United Kingdom">United Kingdom</option><option value="United States" selected="selected">United States</option><option value="US Minor Outlying Islands">US Minor Outlying Islands</option><option value="Uruguay">Uruguay</option><option value="Uzbekistan">Uzbekistan</option><option value="Vanuatu">Vanuatu</option><option value="Venezuela">Venezuela</option><option value="Viet Nam">Viet Nam</option><option value="Virgin Islands, British">Virgin Islands, British</option><option value="Virgin Islands, U.S.">Virgin Islands, U.S.</option><option value="Wallis and Futuna">Wallis and Futuna</option><option value="Western Sahara">Western Sahara</option><option value="Yemen">Yemen</option><option value="Zambia">Zambia</option><option value="Zimbabwe">Zimbabwe</option></select></td>
                </tr>
        <tr>
            <td class="rightAlign">* Phone Number</td>
            <td><input type="text" size="25" name="shipPhoneNumber" id="shipPhoneNumber" data-constraints="@Required(label=&quot;Shipping Phone Number&quot;, groups=[customer])" class="regula-validation checkoutBottom"></td>
        </tr>
        <tr>
            <td colspan="2">&nbsp;</td>
        </tr>
            <tr class="shippingCheckbox">
                <td colspan="2"></td>
            </tr>
    </tbody></table>
        <script type="text/javascript">jQuery('.shippingTable').removeAttr('style');</script>
    <script type="text/javascript">jQuery(document).ready(function() {            var $shipCountry = jQuery('#shipCountry');            if ($shipCountry.val() == 'United States' || $shipCountry.val() == 'Canada') {
                jQuery('#shippingStateRequired').html('* State');
            }            if ($shipCountry.length &gt; 0 &amp;&amp; "SELECT" == $shipCountry.get(0).tagName) {
                $shipCountry.change(function() {                    if ($shipCountry.val() == 'United States' || $shipCountry.val() == 'Canada') {
                        jQuery('#shippingStateRequired').html('* State');
                    } else {
                        jQuery('#shippingStateRequired').html('State');
                    }
                });
            }            var formName = 'checkout';
            jQuery('#shipAddressLine1').bind('change', {formName: formName}, Infusion.ManageCart.upsAjaxCall);
            jQuery('#shipCity').bind('change', {formName: formName}, Infusion.ManageCart.upsAjaxCall);
            jQuery('#shipState').bind('change', {formName: formName}, Infusion.ManageCart.upsAjaxCall);
            jQuery('#shipZipCode').bind('change', {formName: formName}, Infusion.ManageCart.upsAjaxCall);
            jQuery('#shipCountry').bind('change', {formName: formName}, Infusion.ManageCart.upsAjaxCall);
        });</script>
    </div>
    <div id="PAYMENT_SELECTION">
<table class="paymentMethodTable tabular grid">
    <tbody>
        <tr>
            <th class="leftAlign" colspan="4">Payment Information</th>
        </tr>            <tr>
                            <td colspan="4">
                                        <input type="hidden" value="creditcard" name="paymentType" id="creditCardType">
                                <label for="creditCardType">
                                    <img class="paymentIcon" src="/resources/styledcart/images/paymenttypes/creditcard.png">
                                    <span class="smallHeader">Credit card</span>
                                </label>
                    </td>
            </tr>                <tr>
                    <td colspan="4">
                    </td>
                </tr><!-- creditCardForm v2 -->
<tr class="cellLow">
    <td class="pay1">
        <span class="paymentLabel">Credit Card Type</span>
        <select data-on="Component.Select" size="1" name="cardType" id="cardType" class="checkout"><option value="American Express">American Express</option><option value="Discover">Discover</option><option value="MasterCard">MasterCard</option><option value="STRIPE (manual)">STRIPE (manual)</option></select>
    </td>
    <td class="pay2">
        <span class="paymentLabel">Credit Card Number</span>
                <input type="text" autocomplete="off" maxlength="16" name="cardNumber" id="cardNumber" data-constraints="@Required(label=&quot;Credit Card Number&quot;, groups=[creditCard])" class="regula-validation checkout">&nbsp;&nbsp;
    </td>
    <td class="pay3">
        <span class="paymentLabel">Expiration Date</span>
        <select data-on="Component.Select" size="1" name="expirationMonth" id="expirationMonth" class="checkoutShortest"><option value="01">01</option><option value="02">02</option><option value="03">03</option><option value="04">04</option><option value="05">05</option><option value="06">06</option><option value="07">07</option><option value="08">08</option><option value="09">09</option><option value="10">10</option><option value="11">11</option><option value="12">12</option></select>
        <select data-on="Component.Select" size="1" name="expirationYear" id="expirationYear" class="checkoutShortest"><option value="2015">2015</option><option value="2016">2016</option><option value="2017">2017</option><option value="2018">2018</option><option value="2019">2019</option><option value="2020">2020</option><option value="2021">2021</option><option value="2022">2022</option><option value="2023">2023</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option><option value="2027">2027</option><option value="2028">2028</option><option value="2029">2029</option></select>
    </td>
    <td class="pay4">
            <span class="paymentLabel">Security Code <a onclick="return false;" id="tooltip1" class="tooltip"><img border="0" style="margin-left: 5px; cursor: pointer;" alt="tooltip" src="/resources/styledcart/images/tooltip-icon.png"></a></span>
            <input type="text" autocomplete="off" size="3" name="verificationCode" id="verificationCode" data-constraints="@Required(label=&quot;Security Code&quot;, groups=[creditCard])" class="regula-validation checkoutShortest">
    </td>
</tr>
            <script type="text/javascript">Infusion.on("ManageCart").readyExec(function() {                if (jQuery('#cardType').val() !== "Maestro") {
                    maestroNotSelected();
                }                jQuery('#creditCardType').bind("click", function() {
                    // in general, slide effect doesn't work on &lt;tr&gt;
                    jQuery('tr.cellLow').show();
                    if (jQuery('#cardType').val() !== "Maestro") {
                        maestroNotSelected();
                    }
                });                jQuery(document).on("click", '#paybycheck', function() {
                   jQuery('tr.cellLow').hide();
                });                jQuery(document).on('change', '#cardType', function() {
                    if (jQuery('#cardType').val() !== "Maestro") {
                        maestroNotSelected();
                    } else {
                        maestroSelected();
                    }
                });                function maestroSelected() {
                    jQuery('tr.maestro').show();
                }                function maestroNotSelected() {
                    jQuery('tr.maestro').hide();
                }                //Re-bind the regula validation of credit card fields in case this JSP is refreshed through AJAX-ing (which loses the binding)
                regula.bind();                //Re-bind the tooltip for credit card CVC, because AJAX-ing removes the binding.
                Infusion.Ecomm.OrderForms.bindTooltip('tooltip');
        ;});</script>
        <script type="text/javascript">jQuery('.paymentMethodTable').removeAttr('style');</script>
    </tbody>
</table>    </div>
    <div id="CUSTOM_HTML">
<div id="customCheckoutBottom">
</div>
    </div>                        </div>    <div id="CHECKOUT_LINKS"><div class="checkoutLinksBottom">
    <a class="continueButton" href="/app/storeFront/showStoreFront">Continue Shopping</a>                <a onclick="Infusion.ManageCart.goToReviewPage(jQuery('#reviewOrderButton').closest('form').attr('id'));" class="continueButton" id="reviewOrderButton" href="javascript:void(0)">Review Order</a></div>    </div>                        </form>