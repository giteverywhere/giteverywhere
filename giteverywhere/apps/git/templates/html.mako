<!DOCTYPE html>
<html>
<body>
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<% import random %>

 <% r = lambda: random.randint(128,256) %>
 <% q = [] %>
  

        %for j in range(len(comit_record)):
           <% w = '#%02X%02X%02X' % (r(),r(),r()) %>
           <% q.append(w) %>
        %endfor
<div>
<style type = "text/css">
{background-color:${q[0]}}
</style>
<table>
<tr>
<td style = "bgcolor:${q[0]}">${q}</td>
<td>${q}</td>
</tr>
</table>
</div>



</body>
</html>