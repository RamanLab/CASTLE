# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:06:44 2020

@author: Ryzen
"""

import csv

#replace the name with your actual csv file name
file_name = "master.csv" 
f1 = open(file_name)
csv_file = csv.reader(f1)

def slr(line):
    slrtable=""
    file_name1 = "CSV/"+line[0]+"/JSL.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            slrtable = slrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/reactions/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            slrtable = slrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#reaction/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
            idx += 1
            
    return slrtable

def dlr(line):
    dlrtable=""
    file_name1 = "CSV/"+line[0]+"/JDL.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            dlrtable = dlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/reactions/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='"+line[8]+"/reactions/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            dlrtable = dlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#reaction/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='https://vmh.life/#reaction/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
            
    return dlrtable

def tlr(line):
    tlrtable=""
    file_name1 = "CSV/"+line[0]+"/JTL.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            tlrtable = tlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/reactions/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='"+line[8]+"/reactions/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td><td><a href='"+line[8]+"/reactions/"+line1[2].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[2].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            tlrtable = tlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#reaction/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='https://vmh.life/#reaction/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td><td><a href='https://vmh.life/#reaction/"+line1[2].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[2].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
    
    return tlrtable

def slg(line):
    slgtable=""
    file_name1 = "CSV/"+line[0]+"/SGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            slgtable = slgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/genes/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            slgtable = slgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#microbegene/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1

    return slgtable

def dlg(line):
    dlgtable=""
    file_name1 = "CSV/"+line[0]+"/DGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            dlgtable = dlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/genes/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='"+line[8]+"/genes/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            dlgtable = dlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#microbegene/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='https://vmh.life/#microbegene/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1

    return dlgtable

def tlg(line):
    tlgtable=""
    file_name1 = "CSV/"+line[0]+"/TGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            tlgtable = tlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/genes/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='"+line[8]+"/genes/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td><td><a href='"+line[8]+"/genes/"+line1[2].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[2].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            tlgtable = tlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#microbegene/"+line1[0].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[0].strip("'")+"</font></u></center></a></td><td><a href='https://vmh.life/#microbegene/"+line1[1].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[1].strip("'")+"</font></u></center></a></td><td><a href='https://vmh.life/#microbegene/"+line1[2].strip("'")+"' target='blank'><center><u><font color='black'>"+line1[2].strip("'")+"</font></u></center></a></td></tr>"
            idx += 1

    return tlgtable

html_normal = """

    <!doctype html>
<html lang="en">
<head>
  
    <title>CASTLE | {organism1:}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Muli:400,700|Hepta+Slab:400,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="../fonts/icomoon/style.css">
    <link rel="shortcut icon" type="image/x-icon" href="../img/favicon.png">	

    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="../css/jquery.fancybox.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/owl.theme.default.min.css">
    <link rel="stylesheet" href="../fonts/flaticon/font/flaticon.css">
    <link rel="stylesheet" href="../css/aos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/0.71/jquery.csv-0.71.min.js"></script>
	<script src="https://www.w3schools.com/lib/w3data.js"></script>
    <!-- MAIN CSS -->
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/syntheticlethals.css">

<script>
	$(document).scroll(function() {{
	  var y = $(this).scrollTop();
	  if (y > 300) {{
		$('.sidenav').fadeIn();
	  }} else {{
		$('.sidenav').fadeOut();
	  }}
	}});
</script>
  </head>

<body>


    <header>
        <div class="header-area ">
            <div id="sticky-header" class="main-header-area white-bg">
                <div class="container-fluid p-0">
                    <div class="row align-items-center justify-content-between no-gutters">
                        <div class="col-xl-2 col-lg-2">
                            <div class="logo-img">
                                <a href="../index.html">
                                    <img src="../img/logo.png" alt="">
                                </a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-4">
                            <div class="main-menu  d-none d-lg-block">
                                <nav>
                                    <ul id="navigation">
                                        <li><a class="active" href="../index.html">home</a></li>
                                        <li><a href="../about.html">About</a></li>
                                        <li><a href="../contact.html">Contact</a></li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="mobile_menu d-block d-lg-none"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    	<!-- breadcam_area_start -->
    <div class="breadcam_area bradcam_bg overlay2">
        <div class="bradcam_text">
            <h2><mark>{organism1:}</mark></h2>
        </div>
    </div>
    <!-- breadcam_area_end -->
    
      <div class="site-section">
		<div class="col-lg-4 sidenav">
			<h4>Jump to Sections</h4>
			<a href="#downloads">Download Files</a>
			<a href="#slr">Single Lethal Reactions</a>
			<a href="#dlr">Double Lethal Reactions</a>
			<a href="#tlr">Triple Lethal Reactions</a>
			<a href="#slg">Single Lethal Genes</a>
			<a href="#dlg">Double Lethal Genes</a>
			<a href="#tlg">Triple Lethal Genes</a>			  
		</div>
            <div id="downloads" class="container">			
				<div class="col-lg-9 sans">
					<br><br>
					<p style = 'line-height: 10px'>
					<img src = '../img/elements/growth_rate.PNG' width=20 style='vertical-align: middle' /><font size=4> Growth Rate: {gr:}</font></p>
                    <br>
					<p style = 'line-height: 5px'>
					<img src = '../img/elements/pathogen.PNG' width=20 style='vertical-align: middle' /><font size=4> Human Pathogen: {hp:}</font></p>
				</div>
                    <br>
                   <br>
                    <table class="minimalistBlack" border="0" align="center">
                        <tr><td><center><a href="#slr"><font color="maroon"><u>Single lethal reactions</u>
                            <br> (Jsl)</font></a></center></td>
                        <td> <p><a href="../CSV/{organism:}/JSL.csv" download="{organism:}_Jsl.csv"><center><abbr title='Download the Jsl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          <td> <p><a href="../json/{organism:}/JSL.json" download="{organism:}_Jsl.json"><center><abbr title='Download the Jsl JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                            <td rowspan="3"><p><a href="../mat/{organism:}/{organism:}.matRxn_lethals.mat" download="{organism:}.matRxn_lethals.mat"><center><abbr title='Download all the Lethal Reactions MAT file'><img src='../img/elements/matlab.png' height='65' width='70 '></abbr></a>
                              <br><font size="2">(Combined download <br>
                                of Jsl, Jdl and Jtl)</font></p></td>
                        
                        </tr>
                            <tr><td><center><a href="#dlr"><font color="maroon"><u>Double lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JDL.csv" download="{organism:}_Jdl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                                <td> <p><a href="../json/{organism:}/JDL.json" download="{organism:}_Jdl.json"><center><abbr title='Download the Jdl JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                               


                        </tr>
                        <tr><td><center><a href="#tlr"><font color="maroon"><u>Triple lethal<br>reactions</u>
                            <br> (Jtl)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/JTL.csv" download="{organism:}_Jtl.csv"><center><abbr title='Download the Jtl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/JTL.json" download="{organism:}_Jtl.json"><center><abbr title='Download the Jtl JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                        <tr><td><center><a href="#slg"><font color="maroon"><u>Single lethal genes</u>
                            <br> (Sgd)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/SGD.csv" download="{organism:}_Sgd.csv"><center><abbr title='Download the Sgd CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/SGD.json" download="{organism:}_Sgd.json"><center><abbr title='Download the Sgd JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                              <td rowspan="3"><p><a href="../mat/{organism:}/{organism:}.mat_gene_lethals.mat" download="{organism:}.mat_gene_lethals.mat"><center><abbr title='Download all the Lethal Genes MAT file'><img src='../img/elements/matlab.png' height='65' width='70 '></abbr></a>
                                <br><font size="2">(Combined download <br>of Sgd, Dgd and Tgd)</font></p></td>
                        </tr>
                        <tr><td><center><a href="#dlg"><font color="maroon"><u>Double lethal genes</u>
                            <br> (Dgd)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/DGD.csv" download="{organism:}_Dgd.csv"><center><abbr title='Download the Dgd CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/DGD.json" download="{organism:}_Dgd.json"><center><abbr title='Download the Dgd JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                        <tr><td><center><a href="#tlg"><font color="maroon"><u>Triple lethal genes</u><br>(Tgd)</font></a>
                            </center> </td>
                          <td> <p><a href="../CSV/{organism:}/TGD.csv" download="{organism:}_Tgd.csv"><center><abbr title='Download the Tgd CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/TGD.json" download="{organism:}_Tgd.json"><center><abbr title='Download the Tgd JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                    
                    </table>
               
               <br>
			   	<p style = 'line-height: 10px'>
					<img src = '../img/elements/model_link.PNG' width=20 height=20 style='vertical-align: middle' />
                    <font size=4>Model Link:<a href="{link:}" target="blank"> <font color="black"><u>{link:}</u></font></a>
				</font></p>
                        <br>
             <br><br>
             
            </div>
			
            <div class="site-section">
				<div id="slr" class="container">
                    <div>
					<div>
				   <center> 
			   <br><br>
			   <h2>Single Lethal Reactions</h2>
			   <br>
					<table width="50%" align="center">{slrtable:}</table>
					</center>
					</div>
				</div>
					
          </div>
		  
		  <div id="dlr" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Reactions</h2>
			   <br>
                <table width="65%" align="center">{dlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>
			<div id="tlr" class="container">
      
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Reactions</h2>
			   <br>
                <table width="75%" align="center">{tlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>
		
				<div id="slg" class="container">
		  
				  <div>
					<div>
				   <center> 
			   <br><br>
			   <h2>Single Lethal Genes</h2>
			   <br>
					<table width="50%" align="center">{slgtable:}</table>
					</center>
					</div>
				</div>
				</div>
			</div>
			
			<div id="dlg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{dlgtable:}</table>
                </center>
                </div>
            </div>
		</div>
			
			<div id="tlg" class="container">
      
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Genes</h2>
			   <br>
                <table width="75%" align="center">{tlgtable:}</table><br><br>
                </center>
                </div>
            </div>
			
	</div>
  
    <footer class="footer footer_bg">
        <div class="footer_copy_right">
            <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved by CASTLE | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        </div>
    </footer>
          </div> <!-- END .site-section -->

</body>
</html>
    
"""

html_bifido = """

    <!doctype html>
<html lang="en">
<head>
  
    <title>CASTLE | {organism1:}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Muli:400,700|Hepta+Slab:400,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="../fonts/icomoon/style.css">
    <link rel="shortcut icon" type="image/x-icon" href="../img/logo.png">	

    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="../css/jquery.fancybox.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/owl.theme.default.min.css">
    <link rel="stylesheet" href="../fonts/flaticon/font/flaticon.css">
    <link rel="stylesheet" href="../css/aos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/0.71/jquery.csv-0.71.min.js"></script>
	<script src="https://www.w3schools.com/lib/w3data.js"></script>
    <!-- MAIN CSS -->
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/syntheticlethals.css">

<script>
	$(document).scroll(function() {{
	  var y = $(this).scrollTop();
	  if (y > 300) {{
		$('.sidenav').fadeIn();
	  }} else {{
		$('.sidenav').fadeOut();
	  }}
	}});
</script>
  </head>

<body>


    <header>
        <div class="header-area ">
            <div id="sticky-header" class="main-header-area white-bg">
                <div class="container-fluid p-0">
                    <div class="row align-items-center justify-content-between no-gutters">
                        <div class="col-xl-2 col-lg-2">
                            <div class="logo-img">
                                <a href="../index.html">
                                    <img src="../img/logo.png" alt="">
                                </a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-4">
                            <div class="main-menu  d-none d-lg-block">
                                <nav>
                                    <ul id="navigation">
                                        <li><a class="active" href="../index.html">home</a></li>
                                        <li><a href="../about.html">About</a></li>
                                        <li><a href="../contact.html">Contact</a></li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="mobile_menu d-block d-lg-none"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    	<!-- breadcam_area_start -->
    <div class="breadcam_area bradcam_bg overlay2">
        <div class="bradcam_text">
            <h2><mark>{organism1:}</mark></h2>
        </div>
    </div>
    <!-- breadcam_area_end -->
    
      <div class="site-section">
		<div class="col-lg-4 sidenav">
			<h4>Jump to Sections</h4>
			<a href="#downloads">Download Files</a>
            <a href="#network">Interaction Network</a>
			<a href="#slr">Single Lethal Reactions</a>
			<a href="#dlr">Double Lethal Reactions</a>		  
			<a href="#tlr">Triple Lethal Reactions</a>
			<a href="#slg">Single Lethal Genes</a>
        	<a href="#dlg">Double Lethal Genes</a>
			<a href="#tlg">Triple Lethal Genes</a>
        </div>
            <div id="downloads" class="container">			
                    <br>
                   <br>
                    <table class="minimalistBlack" border="0" align="center">
                        <tr><td><center><a href="#slr"><font color="maroon"><u>Single lethal reactions</u>
                            <br> (Jsl)</font></a></center></td>
                            <td> <p><a href="../CSV/{organism:}/JSL.csv" download="{organism:}_Jsl.csv"><center><abbr title='Download the Jsl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                        
                        </tr>
                        <tr><td><center><a href="#dlr"><font color="maroon"><u>Double lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JDL.csv" download="{organism:}_Jdl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#tlr"><font color="maroon"><u>Triple lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JTL.csv" download="{organism:}_Jtl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#slg"><font color="maroon"><u>Single lethal genes</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/SGD.csv" download="{organism:}_Sgd.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#dlg"><font color="maroon"><u>Double lethal genes</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/DGD.csv" download="{organism:}_Dgd.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#tlg"><font color="maroon"><u>Triple lethal genes</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/TGD.csv" download="{organism:}_Tgd.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                    
                    </table>
               
               <br>
			   	<p style = 'line-height: 10px'>
					<img src = '../img/elements/model_link.PNG' width=20 height=20 style='vertical-align: middle' />
                    <font size=4>Model Link:<a href="{link:}" target="blank"> <font color="black"><u>{link:}</u></font></a>
				</font></p>
                        <br>
                        
            </div>

            
            
            <div id="network">
                        
                <iframe style="display: block; margin: auto; width: 35%; height: 620px" scrolling=no
                    src="../networks/{organism:}/networkx_graph.html" seamless="seamless">
                </iframe>
                <p class="container" style="text-align: center; width: 35%;">This figure depicts the lethal sets in the form of interaction network. Each synthetic lethal gene in the organism is shown as a node and these nodes are connected to other genes with which they form a lethal set. This interactive figure shows the name, function and KEGG ID of the gene on hovering over the node. Clicking on a node highlights its connections. <b style="color: #000">You can download the edgelist files for double lethals and triple lethals below.</b></p>
            
            </div><br>
            
            <div class="row" style="width: 50%; margin: auto;">
                   <div class="col-lg-6" style="text-align: center">
                       <img src="../img/elements/text.png" width="20" style="vertical-align: middle"><h4><u><a href="../networks/{organism:}/DLG.edgelist">Download DGD gene network (edgelist)</a></u></h4>
                   </div>
                   <div class="col-lg-6" style="text-align: center">
                       <img src="../img/elements/text.png" width="20" style="vertical-align: middle"><h4><u><a href="../networks/{organism:}/TLG.edgelist">Download TGD gene network (edgelist)</a></u></h4>
                   </div>
               </div>
            </div>
             
			
            <div class="site-section">
				<div id="slr" class="container">
                    <div>
					<div>
				   <center> 
			   <br><br>
			   <h2>Single Lethal Reactions</h2>
			   <br>
					<table width="50%" align="center">{slrtable:}</table>
					</center>
					</div>
				</div>
					
          </div>
		  
		  <div id="dlr" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Reactions</h2>
			   <br>
                <table width="65%" align="center">{dlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>
          
		  <div id="tlr" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Reactions</h2>
			   <br>
                <table width="65%" align="center">{tlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>

		  <div id="slg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Single Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{slgtable:}</table>
                </center>
                </div>
            </div>
                
          </div>

		  <div id="dlg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{dlgtable:}</table>
                </center>
                </div>
            </div>
                
          </div>

		  <div id="tlg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{tlgtable:}</table>
                </center>
                </div>
            </div>
                
          </div>          
  
    <footer class="footer footer_bg">
        <div class="footer_copy_right">
            <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved by CASTLE | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        </div>
    </footer>
          </div> <!-- END .site-section -->

</body>
</html>

"""

html_net = """

    <!doctype html>
<html lang="en">
<head>
  
    <title>CASTLE | {organism1:}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Muli:400,700|Hepta+Slab:400,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="../fonts/icomoon/style.css">
    <link rel="shortcut icon" type="image/x-icon" href="../img/favicon.png">	

    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="../css/jquery.fancybox.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/owl.theme.default.min.css">
    <link rel="stylesheet" href="../fonts/flaticon/font/flaticon.css">
    <link rel="stylesheet" href="../css/aos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/0.71/jquery.csv-0.71.min.js"></script>
	<script src="https://www.w3schools.com/lib/w3data.js"></script>
    <!-- MAIN CSS -->
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/syntheticlethals.css">

<script>
	$(document).scroll(function() {{
	  var y = $(this).scrollTop();
	  if (y > 300) {{
		$('.sidenav').fadeIn();
	  }} else {{
		$('.sidenav').fadeOut();
	  }}
	}});
</script>
  </head>

<body>


    <header>
        <div class="header-area ">
            <div id="sticky-header" class="main-header-area white-bg">
                <div class="container-fluid p-0">
                    <div class="row align-items-center justify-content-between no-gutters">
                        <div class="col-xl-2 col-lg-2">
                            <div class="logo-img">
                                <a href="../index.html">
                                    <img src="../img/logo.png" alt="">
                                </a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-4">
                            <div class="main-menu  d-none d-lg-block">
                                <nav>
                                    <ul id="navigation">
                                        <li><a class="active" href="../index.html">home</a></li>
                                        <li><a href="../about.html">About</a></li>
                                        <li><a href="../contact.html">Contact</a></li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="mobile_menu d-block d-lg-none"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    	<!-- breadcam_area_start -->
    <div class="breadcam_area bradcam_bg overlay2">
        <div class="bradcam_text">
            <h2><mark>{organism1:}</mark></h2>
        </div>
    </div>
    <!-- breadcam_area_end -->
    
      <div class="site-section">
		<div class="col-lg-4 sidenav">
			<h4>Jump to Sections</h4>
			<a href="#downloads">Download Files</a>
            <a href="#network">Interaction Network</a>
			<a href="#slr">Single Lethal Reactions</a>
			<a href="#dlr">Double Lethal Reactions</a>
			<a href="#tlr">Triple Lethal Reactions</a>
			<a href="#slg">Single Lethal Genes</a>
			<a href="#dlg">Double Lethal Genes</a>
			<a href="#tlg">Triple Lethal Genes</a>			  
		</div>
            <div id="downloads" class="container">			
				<div class="col-lg-9 sans">
					<br><br>
					<p style = 'line-height: 10px'>
					<img src = '../img/elements/growth_rate.PNG' width=20 style='vertical-align: middle' /><font size=4> Growth Rate: {gr:}</font></p>
                    <br>
					<p style = 'line-height: 5px'>
					<img src = '../img/elements/pathogen.PNG' width=20 style='vertical-align: middle' /><font size=4> Human Pathogen: {hp:}</font></p>
				</div>
                    <br>
                   <br>
                    <table class="minimalistBlack" border="0" align="center">
                        <tr><td><center><a href="#slr"><font color="maroon"><u>Single lethal reactions</u>
                            <br> (Jsl)</font></a></center></td>
                        <td> <p><a href="../CSV/{organism:}/JSL.csv" download="{organism:}_Jsl.csv"><center><abbr title='Download the Jsl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          <td> <p><a href="../json/{organism:}/JSL.json" download="{organism:}_Jsl.json"><center><abbr title='Download the Jsl JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                            <td rowspan="3"><p><a href="../mat/{organism:}/{organism:}.matRxn_lethals.mat" download="{organism:}.matRxn_lethals.mat"><center><abbr title='Download all the Lethal Reactions MAT file'><img src='../img/elements/matlab.png' height='65' width='70 '></abbr></a>
                              <br><font size="2">(Combined download <br>
                                of Jsl, Jdl and Jtl)</font></p></td>
                        
                        </tr>
                            <tr><td><center><a href="#dlr"><font color="maroon"><u>Double lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JDL.csv" download="{organism:}_Jdl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                                <td> <p><a href="../json/{organism:}/JDL.json" download="{organism:}_Jdl.json"><center><abbr title='Download the Jdl JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                               


                        </tr>
                        <tr><td><center><a href="#tlr"><font color="maroon"><u>Triple lethal<br>reactions</u>
                            <br> (Jtl)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/JTL.csv" download="{organism:}_Jtl.csv"><center><abbr title='Download the Jtl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/JTL.json" download="{organism:}_Jtl.json"><center><abbr title='Download the Jtl JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                        <tr><td><center><a href="#slg"><font color="maroon"><u>Single lethal genes</u>
                            <br> (Sgd)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/SGD.csv" download="{organism:}_Sgd.csv"><center><abbr title='Download the Sgd CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/SGD.json" download="{organism:}_Sgd.json"><center><abbr title='Download the Sgd JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                              <td rowspan="3"><p><a href="../mat/{organism:}/{organism:}.mat_gene_lethals.mat" download="{organism:}.mat_gene_lethals.mat"><center><abbr title='Download all the Lethal Genes MAT file'><img src='../img/elements/matlab.png' height='65' width='70 '></abbr></a>
                                <br><font size="2">(Combined download <br>of Sgd, Dgd and Tgd)</font></p></td>
                        </tr>
                        <tr><td><center><a href="#dlg"><font color="maroon"><u>Double lethal genes</u>
                            <br> (Dgd)</font></a></center> </td>
                          <td> <p><a href="../CSV/{organism:}/DGD.csv" download="{organism:}_Dgd.csv"><center><abbr title='Download the Dgd CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/DGD.json" download="{organism:}_Dgd.json"><center><abbr title='Download the Dgd JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                        <tr><td><center><a href="#tlg"><font color="maroon"><u>Triple lethal genes</u><br>(Tgd)</font></a>
                            </center> </td>
                          <td> <p><a href="../CSV/{organism:}/TGD.csv" download="{organism:}_Tgd.csv"><center><abbr title='Download the Tgd CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                            <td> <p><a href="../json/{organism:}/TGD.json" download="{organism:}_Tgd.json"><center><abbr title='Download the Tgd JSON file'><img src='../img/elements/json.png' height='35' width='27 '></abbr></a></p></td>
                           
                        </tr>
                    
                    </table>
             <br>
             <br>
             <br>
             
             </div>

            
            
            <div id="network">
                        
                <iframe style="display: block; margin: auto; width: 35%; height: 620px" scrolling=no
                    src="../networks/{organism:}/networkx_graph.html" seamless="seamless">
                </iframe>
                <p class="container" style="text-align: center; width: 35%;">This figure depicts the lethal sets in the form of interaction network. Each synthetic lethal gene in the organism is shown as a node and these nodes are connected to other genes with which they form a lethal set. This interactive figure shows the name, function and KEGG ID of the gene on hovering over the node. Clicking on a node highlights its connections. <b style="color: #000">You can download the edgelist files for double lethals and triple lethals below.</b></p>
            
            </div><br>
            
            <div class="row" style="width: 50%; margin: auto;">
                   <div class="col-lg-6" style="text-align: center">
                       <img src="../img/elements/text.png" width="20" style="vertical-align: middle"><h4><u><a href="../networks/{organism:}/DLG.edgelist">Download DGD gene network (edgelist)</a></u></h4>
                   </div>
                   <div class="col-lg-6" style="text-align: center">
                       <img src="../img/elements/text.png" width="20" style="vertical-align: middle"><h4><u><a href="../networks/{organism:}/TLG.edgelist">Download TGD gene network (edgelist)</a></u></h4>
                   </div>
               </div>
            </div>
             
            </div>
			
            <div class="site-section">
				<div id="slr" class="container">
                    <div>
					<div>
				   <center> 
			   <br><br>
			   <h2>Single Lethal Reactions</h2>
			   <br>
					<table width="50%" align="center">{slrtable:}</table>
					</center>
					</div>
				</div>
					
          </div>
		  
		  <div id="dlr" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Reactions</h2>
			   <br>
                <table width="65%" align="center">{dlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>
			<div id="tlr" class="container">
      
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Reactions</h2>
			   <br>
                <table width="75%" align="center">{tlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>
		
				<div id="slg" class="container">
		  
				  <div>
					<div>
				   <center> 
			   <br><br>
			   <h2>Single Lethal Genes</h2>
			   <br>
					<table width="50%" align="center">{slgtable:}</table>
					</center>
					</div>
				</div>
				</div>
			</div>
			
			<div id="dlg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{dlgtable:}</table>
                </center>
                </div>
            </div>
		</div>
			
			<div id="tlg" class="container">
      
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Genes</h2>
			   <br>
                <table width="75%" align="center">{tlgtable:}</table><br><br>
                </center>
                </div>
            </div>
			
	</div>
  
    <footer class="footer footer_bg">
        <div class="footer_copy_right">
            <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved by CASTLE | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        </div>
    </footer>
          </div> <!-- END .site-section -->

</body>
</html>
    
"""

for line in csv_file:
    line[0] = line[0].replace('&nbsp;', '_')
    try:
        if 'Bifido' in line[0] and line[-1] == 'vmh':
            full_html = html_bifido.format(organism = line[0], organism1 = ' '.join([i for i in line[0].split('_')]), gr = line[7],hp = line[9],link = line[8],
                                    slrtable=slr(line), dlrtable=dlr(line), tlrtable=tlr(line), slgtable=slg(line), dlgtable=dlg(line), tlgtable=tlg(line))
            filename='Synthetic_Lethal/'+line[0]+'.html'
            print(filename + '- Bifido')
            f = open(filename,'w')
            f.write(full_html)
            f.close()
        elif line[-1] == 'vmh' and 'Bifido' not in line[0]:
            full_html = html_net.format(organism = line[0], organism1 = ' '.join([i for i in line[0].split('_')]), gr = line[7],hp = line[9],link = line[8],
                                    slrtable=slr(line), dlrtable=dlr(line), tlrtable=tlr(line), slgtable=slg(line), dlgtable=dlg(line), tlgtable=tlg(line))
            filename='Synthetic_Lethal/'+line[0]+'.html'
            print(filename + '- Net')
            f = open(filename,'w')
            f.write(full_html)
            f.close()
        else:
            full_html = html_normal.format(organism = line[0], organism1 = ' '.join([i for i in line[0].split('_')]), gr = line[7],hp = line[9],link = line[8],
                                    slrtable=slr(line), dlrtable=dlr(line), tlrtable=tlr(line), slgtable=slg(line), dlgtable=dlg(line), tlgtable=tlg(line))
            filename='Synthetic_Lethal/'+line[0]+'.html'
            print(filename + '- Normal')
            f = open(filename,'w')
            f.write(full_html)
            f.close()
        
    except FileNotFoundError:
        print(line[0]);
    
    
#    break;
    
f1.close()
