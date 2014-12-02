title: Diamand anvil Raman pressure scale
url: tools/diamond.html
save_as: tools/diamond.html

##Tools
<fieldset>
	<legend>Diamond anvil Raman pressure scale</legend>
	Reference diamond Raman peak (cm<sup>-1</sup>):
  	<input id="dia_lambda0" class="input-small" name="dia_lambda0" type="number" value="1334">
    <br />
    Measured position (cm<sup>-1</sup>):
	<input id="dia_lambda" class="input-small" name="dia_lambda" type="number" value="1334">
    <p>
	<strong>
		Pressure =  <span id="dia_pressure"> 0.0 GPa </span>
    </strong>
    </p>
    <h6>Calibration is from:</h6>
		<i>Akahama Y. and Kawamura H., J. Appl. Phys. 100, 043516 (2006).</i>
</fieldset>

<script src="http://code.jquery.com/jquery.min.js"></script>
<script>
	/* Diamond pressure */ 
	$(document).ready(function(){
		$('[id^=dia_]').bind("keyup change", function(){
			diK = 547;
			diKp = 3.74;
			dia0 = parseFloat($('#dia_lambda0').val());
			dia = parseFloat($('#dia_lambda').val());
			diaP = (diK*(dia-dia0)/dia0)*(1 + 0.5*(diKp-1)*(dia-dia0)/dia0);
			$('#dia_pressure').text(diaP.toFixed(2) + " GPa");
		});
	});
</script>
