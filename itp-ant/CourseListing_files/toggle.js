	<!-- HIDE / SHOW background image -->
                 var contentOn = true;
		 function toggleBG(){
                                var c =document.getElementById("content");
                                var f =document.getElementById("foot");
                        if( contentOn ){ 
                                //document.write("turn off");
                                c.className="hide";     
				if (f) 
                                   f.className="hide";     
                                contentOn = false;                             
                         } else {
                                //document.write("turn on");
                                c.className="show";     
				if (f)
	                           f.className="show";     
                                contentOn = true;
                        }
                }    
	<!-- HIDE / SHOW DIV -->
		function showDiv(menuID) {
	  		if (document.getElementById) {
	    		document.getElementById(menuID).style.visibility = "visible";
	  		}
	  		showing = menuID;
		}

		function hideDiv() {
	  		if (document.getElementById) {
	    		document.getElementById(showing).style.visibility = "hidden";
	  		}
		}
	
