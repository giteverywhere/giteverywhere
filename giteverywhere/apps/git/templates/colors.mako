 <html>
 <head><title>Random Color Chart</title></head>
 <body>
 <% from random import randint %>

 <% def genRandomColor(): %>
   <%  a = [0, 0, 0, 0, 0, 0] %>
     %for i in range(0, 6): 
     <%   num1 = randint(0, 1) %>
       %if num1 == 0:
        
 <%      num2 = randint(48, 57) %>
       %else:
 <%       
 <%      num2 = randint(65, 70) %>
 <%      a[i] = num2 %>
 <%      b = [a, a, a, a, a, a] %>
      %endfor
      %for i in range(0, 6): 
             <%    b[i] = chr(a[i]) %>
              <%  thestr = "#"  %>
      %endfor
      %for i in range(0, 6):
 <%   thestr = thestr + b[i] %>  
      %endfor
 <% return thestr %>




<table border = \1\><tr><th>Color Name</th><th>Color</th></tr>

   <% x = genRandomColor() %>
   
    <tr><td> x </td><td style = background-color:  x ></td></tr>
</table>
</body></html>

<div>
<style type = "text/css">
td
{background-color:${q[0]}}
</style>
<table>
<tr>
<td>${q[0]}</td>


</tr>
</table>
</div>

