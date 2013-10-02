
<!DOCTYPE html>
<html>
<body>
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>



<% b = [{'branch':'','bcolor':'','col_pos':''}] %>
<% count = 0 %>

<% import random %>

 <% r = lambda: random.randint(128,256) %>
 <% q = [] %>
 

<div style="float: left;">
<style>
             .circle{
               width: 5px;
               height: 5px;
               border-radius: 50%;
               background-color: blue
               
                  }
</style>
 
%for i in range(len(comit_record)):
<table cellspacing = 0 >

  <tr>
  %for j in range(len(b)):
           <% w = '#%02X%02X%02X' % (r(),r(),r()) %>
           <% q.append(w) %>
   
         
    %if (comit_record[i]['branches']!=b[j]['branch']):
       %if (j == len(b)-1): 
       
          <td style = "width:5px; background-color: ${q[j]}" >
          <div class="circle">
          </div>
          </td>        
         <td><hr style = "width:10px;height:2px;"></td>
         <td  style = "border:1" bgcolor = "lightpink" >${comit_record[i]['branches']}</td>
         <td>&nbsp;${comit_record[i]['message']}</td>
         
         <% count = count + 1 %>
         <% b.append(dict(branch=comit_record[i]['branches'], bcolor=q[j], col_pos=count)) %>
         
   </tr>  
       
       %else:
         
         %if (comit_record[i]['branches'] == b[j+1]['branch']):
            <td style = "width:5px; background-color: ${q[j]}" >
            <div class="circle"></div>
           
           </td>
           <td style = "width:2px;"></td>
                 
         %else:
           <td style = "width:5px; background-color: ${q[j]}" >
           <td style = "width:2px;"></td> 
           
           
         %endif
       %endif
   
    %else: 
       
        %for s in range(len(b)-j):
          %if (s == j-1 and len(b) != 2):
           
            <td style = "width:5px; background-color: ${q[j]}" >
          %else:
            <td>&nbsp;&nbsp;&nbsp;</td>
          %endif
        %endfor
        <td>${comit_record[i]['message']}</td>
         <% break %>
        
    
    </tr>
    
    %endif
  %endfor
</table>
%endfor
</div>

 <div>


<table> 

    <tr>
      %for comit in comit_record:
      
      <td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ${comit['datetime']}</td>
    </tr>
      %endfor
  </table>
</div>




</body>
</html>
      
  
      
  

