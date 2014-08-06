<!DOCTYPE html>

{% load static %}

<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
        <link rel="stylesheet" href="{% static "css/bootstrap.css" %}" /> <!-- CSS -->
        <link rel="stylesheet" href="{% static "css/bootstrap.min.css" %}" /> <!-- CSS -->
        <!--<link rel="stylesheet" href="{% static "css/bootstrap-fluid-adj.css" %}" /> <!-- CSS -->
        <!--<link rel="stylesheet" href="{% static "css/bootstrap-responsive.css" %}" /> <!-- CSS -->
        <!--<link rel="stylesheet" href="{% static "css/bootstrap-responsive.min.css" %}" /> <!-- CSS -->

        <!-- Add custom CSS here -->
        <link rel="stylesheet" href="{% static "css/sb-admin.css" %}" /> <!-- CSS -->
        <link rel="stylesheet" href="{% static "font-awesome/css/font-awesome.min.css" %}">
        <!-- Page Specific CSS -->
        <link rel="stylesheet" href="{% static "http://cdn.oesmith.co.uk/morris-0.4.3.min.css" %}">

        <title>pos_app - {% block title %}How to Tango with Django!{% endblock %}</title>
</head>
<body>


    <div id="wrapper">
      <!-- Sidebar -->
      <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="index.html">POS</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav side-nav">
            <li class="active"><a href="index.html"><i class="fa fa-dashboard"></i> The Links will be here</a></li>
            <li><a href="/pos_app/add_person/">Register User</a></li>
            <li><a href="/pos_app/testing/">Testing</a></li>
            <li><a href="charts.html"><i class="fa fa-bar-chart-o"></i> Charts</a></li>
            <li><a href="tables.html"><i class="fa fa-table"></i> Tables</a></li>
            <li><a href="forms.html"><i class="fa fa-edit"></i> Forms</a></li>
            <li><a href="typography.html"><i class="fa fa-font"></i> Typography</a></li>
            <li><a href="bootstrap-elements.html"><i class="fa fa-desktop"></i> Bootstrap Elements</a></li>
            <li><a href="bootstrap-grid.html"><i class="fa fa-wrench"></i> Bootstrap Grid</a></li>
            <li><a href="blank-page.html"><i class="fa fa-file"></i> Blank Page</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-caret-square-o-down"></i> Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Dropdown Item</a></li>
                <li><a href="#">Another Item</a></li>
                <li><a href="#">Third Item</a></li>
                <li><a href="#">Last Item</a></li>
              </ul>
            </li>
          </ul>-->

          <ul class="nav navbar-nav navbar-right navbar-user">
            <li class="dropdown messages-dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-envelope"></i> Messages <span class="badge">7</span> <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">7 New Messages</li>
                <li class="message-preview">
                  <a href="#">
                    <span class="avatar"><img src="http://placehold.it/50x50"></span>
                    <span class="name">John Smith:</span>
                    <span class="message">Hey there, I wanted to ask you something...</span>
                    <span class="time"><i class="fa fa-clock-o"></i> 4:34 PM</span>
                  </a>
                </li>
                <li class="divider"></li>
                <li class="message-preview">
                  <a href="#">
                    <span class="avatar"><img src="http://placehold.it/50x50"></span>
                    <span class="name">John Smith:</span>
                    <span class="message">Hey there, I wanted to ask you something...</span>
                    <span class="time"><i class="fa fa-clock-o"></i> 4:34 PM</span>
                  </a>
                </li>
                <li class="divider"></li>
                <li class="message-preview">
                  <a href="#">
                    <span class="avatar"><img src="http://placehold.it/50x50"></span>
                    <span class="name">John Smith:</span>
                    <span class="message">Hey there, I wanted to ask you something...</span>
                    <span class="time"><i class="fa fa-clock-o"></i> 4:34 PM</span>
                  </a>
                </li>
                <li class="divider"></li>
                <li><a href="#">View Inbox <span class="badge">7</span></a></li>
              </ul>
            </li>
            <li class="dropdown alerts-dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-bell"></i> Alerts <span class="badge">3</span> <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Default <span class="label label-default">Default</span></a></li>
                <li><a href="#">Primary <span class="label label-primary">Primary</span></a></li>
                <li><a href="#">Success <span class="label label-success">Success</span></a></li>
                <li><a href="#">Info <span class="label label-info">Info</span></a></li>
                <li><a href="#">Warning <span class="label label-warning">Warning</span></a></li>
                <li><a href="#">Danger <span class="label label-danger">Danger</span></a></li>
                <li class="divider"></li>
                <li><a href="#">View All</a></li>
              </ul>
            </li>
            <li class="dropdown user-dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> John Smith <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#"><i class="fa fa-user"></i> Profile</a></li>
                <li><a href="#"><i class="fa fa-envelope"></i> Inbox <span class="badge">7</span></a></li>
                <li><a href="#"><i class="fa fa-gear"></i> Settings</a></li>
                <li class="divider"></li>
                <li><a href="#"><i class="fa fa-power-off"></i> Log Out</a></li>
              </ul>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </nav>


      <div id="page-wrapper">

        <div class="row">
          <div class="col-lg-12">
            <h1>Forms <small>Enter Your Data</small></h1>
            <ol class="breadcrumb">
              <li><a href="index.html"><i class="fa fa-dashboard"></i> Dashboard</a></li>
              <li class="active"><i class="fa fa-edit"></i> Forms</li>
            </ol>
            <div class="alert alert-info alert-dismissable">
              <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
              Visit <a class="alert-link" target="_blank" href="http://getbootstrap.com/css/#forms">Bootstrap's Form Documentation</a> for more information.
            </div>
          </div>
        </div><!-- /.row -->

        <div class="row">
          <div class="col-lg-6">

            <form role="form" id="category_form" method="post" action="/pos_app/add_person/">

              <div class="form-group">
                <label>Text Input</label>
                <input class="form-control">
                <p class="help-block">Example block-level help text here.</p>
              </div>
                {% csrf_token %}
                
                {% for hidden in form.hidden_fields %}
                <div class="form-group">
                <label>{{ field.help_text }}</label>                
                    <!--{{ field.errors }}-->
                    {{ hidden }}                
                <!--<p class="help-block">Example block-level help text here.</p>-->
                </div>
                {% endfor %}
    
                {% for field in form.visible_fields %}
                <div class="form-group">
                <label>{{ field.help_text }}</label>                
                    {{ field.errors }}
                    {{ field }}                
                <p class="help-block">Example block-level help text here.</p>
                </div>
                {% endfor %}
              

              <button type="submit" class="btn btn-default">Submit Button</button>
              <button type="reset" class="btn btn-default">Reset Button</button>  

            </form>

          </div>
          <div class="col-lg-6">
            <h1>Disabled Form States</h1>

            <form role="form">

              <fieldset disabled>

                <div class="form-group">
                  <label for="disabledSelect">Disabled input</label>
                <input class="form-control" id="disabledInput" type="text" placeholder="Disabled input" disabled>
                </div>

                <div class="form-group">
                  <label for="disabledSelect">Disabled select menu</label>
                  <select id="disabledSelect" class="form-control">
                    <option>Disabled select</option>
                  </select>
                </div>

                <div class="checkbox">
                  <label>
                    <input type="checkbox"> Disabled Checkbox
                  </label>
                </div>

                <button type="submit" class="btn btn-primary">Disabled Button</button>

              </fieldset>

            </form>

            <h1>Form Validation</h1>

            <form role="form">

              <div class="form-group has-success">
                <label class="control-label" for="inputSuccess">Input with success</label>
                <input type="text" class="form-control" id="inputSuccess">
              </div>

              <div class="form-group has-warning">
                <label class="control-label" for="inputWarning">Input with warning</label>
                <input type="text" class="form-control" id="inputWarning">
              </div>

              <div class="form-group has-error">
                <label class="control-label" for="inputError">Input with error</label>
                <input type="text" class="form-control" id="inputError">
              </div>
            
            </form>
            
            <h1>Input Groups</h1>

            <form role="form">

              <div class="form-group input-group">
                <span class="input-group-addon">@</span>
                <input type="text" class="form-control" placeholder="Username">
              </div>

              <div class="form-group input-group">
                <input type="text" class="form-control">
                <span class="input-group-addon">.00</span>
              </div>

              <div class="form-group input-group">
                <span class="input-group-addon"><i class="fa fa-eur"></i></span>
                <input type="text" class="form-control" placeholder="Font Awesome Icon">
              </div>

              <div class="form-group input-group">
                <span class="input-group-addon">$</span>
                <input type="text" class="form-control">
                <span class="input-group-addon">.00</span>
              </div>
              
              <div class="form-group input-group">
                <input type="text" class="form-control">
                <span class="input-group-btn">
                  <button class="btn btn-default" type="button"><i class="fa fa-search"></i></button>
                </span>
              </div>

            </form>
            
            <p>For complete documentation, please visit <a href="http://getbootstrap.com/css/#forms">Bootstrap's Form Documentation</a>.</p>

          </div>
        </div><!-- /.row -->

      </div><!-- /#page-wrapper -->

    </div><!-- /#wrapper -->
  


        <!--Additional javascript -->
        <script src="{% static "js/bootstrap.js" %}"></script> <!-- JavaScript -->
        <!-- JavaScript -->
        <script src="{% static "js/jquery-1.10.2.js" %}"></script>
        <script src="{% static "js/bootstrap.js" %}"></script>

        <!-- Page Specific Plugins -->
        <script src="{% static "http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js" %}"></script>
        <script src="{% static "http://cdn.oesmith.co.uk/morris-0.4.3.min.js" %}"></script>
        <script src="{% static "js/morris/chart-data-morris.js" %}"></script>
        <script src="{% static "js/tablesorter/jquery.tablesorter.js" %}"></script>
        <script src="{% static "js/tablesorter/tables.js" %}"></script>
</body>
</html>