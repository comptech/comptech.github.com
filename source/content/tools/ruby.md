title: Ruby fluorescence pressure calculator
url: tools/ruby.html
save_as: tools/ruby.html

## Tools
<fieldset>
<legend>Ruby fluorescence pressure calculator</legend>
	<label>Conditions:</label>
	<select id="ruby_cond" name="ruby_cond" size="1">
  		<option value="hydro">hydrostatic</option>
  	  	<option value="nonhydro">non-hydrostatic</option>
  	</select>
	<br />
	Reference ruby:
	<input id="ruby_lambda0" class="input-small" name="ruby_lambda0" type="number" value="694.22"> nm, at T=
	<input id="ruby_reftemp" class="input-small" name="ruby_reftemp" type="number" value="298">(K)
	<br />
	Measured ruby:
	<input id="ruby_lambda" class="input-small" name="ruby_lambda" type="number" value="694.22"> nm, at T=
	<input id="ruby_temp" class="input-small" name="ruby_temp" type="number" value="298">(K) 
	<p>
		<strong>
			Pressure =  <span id="ruby_pressure">0.0 GPa</span>
		</strong>
	</p>
	<h6>Pressure dependence of ruby shift is from </h6>
	<i>Mao H.K., Xu J., and Bell P.M. (1986) J. Geophys. Res. 91, 4673</i>
	<h6> Temperature correction is from</h6>
	<i>Rekhi S., Dubrovinsky L.S., and Saxena S.K. (1999) High Temp. - High Pres. 31, 299</i>
</fieldset>

<script src="http://code.jquery.com/jquery.min.js"></script>
<script>
	/* Ruby Scale */
	$(document).ready(function(){
		$('[id^=ruby_]').bind("keyup change", function(){
			A = 1904;
			k = 0.46299;
			l = 0.0060823;
			m = 0.0000010264;
			if ($('#ruby_cond').val() == "hydro") {
				B = 7.665;
				} else if ($('#ruby_cond').val() == "nonhydro") {
					B = 5;
				}
				reftemp = parseFloat($('#ruby_reftemp').val());
				temp = parseFloat($('#ruby_temp').val());
				lam0 = parseFloat($('#ruby_lambda0').val());
				lam = parseFloat($('#ruby_lambda').val());
				
				Acorr = A + k*(temp-reftemp);
				lam0corr = lam0 + l*(temp-reftemp) + m*((temp-reftemp)*(temp-reftemp));
				rat = Math.pow(lam/lam0corr, B);
				P = (Acorr/B)*rat-(Acorr/B);
				$('#ruby_pressure').text(P.toFixed(2) + " GPa");
		});
	}); 
</script>