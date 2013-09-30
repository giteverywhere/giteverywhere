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
<table>
<tr>

<td style = "width:10px;height:20px; background-color: ${q[0]}" >${q[0]}</td>

</tr>
</table>
</div>

<td style = "width:5px" bgcolor = ${q[j]} >

</body>
</html>