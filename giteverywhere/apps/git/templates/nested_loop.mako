
<!DOCTYPE html>
<html>
<body>

<title>${self.title()}</title>
<%def name="title()">
The git app
</%def>



<% b = [{'branch':'','bcolor':'','col_pos':''}] %>
<% count = 0 %>
<% c = 0 %>
<% color = ['pink','yellow','orange','red','green','purple','grey'] %>
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
           
          <td style = "width:5px" bgcolor = ${q[j]} >
          <div class="circle">
          </div>
          </td>        
         <td><hr width = "10px"></td>
         <td  style = "border:1" bgcolor = "lightpink" >${comit_record[i]['branches']}</td>
         <td>&nbsp;${comit_record[i]['message']}</td>
         
         <% count = count + 1 %>
         <% b.append(dict(branch=comit_record[i]['branches'], bcolor=q[j], col_pos=count)) %>
         
   </tr>  
       
       %else:
         
         %if (comit_record[i]['branches'] == b[j+1]['branch']):
            <td bgcolor = ${q[j]} width = "5px" >
            <div class="circle"></div>
           
           </td>
           <td style = "width:2px;"></td>
                 
         %else:
           <td style = "width:5px;" bgcolor = ${q[j]}></td>
           <td style = "width:2px;"></td> 
           
           
         %endif
       %endif
   
    %else: 
       
        %for s in range(len(b)-j):
          %if (s == j-1 and len(b) != 2):
           
            <td style = "width:5px;" bgcolor = ${q[j]} ></td>
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
      
  
      
  

