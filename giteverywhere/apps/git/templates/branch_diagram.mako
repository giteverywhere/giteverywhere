
<!DOCTYPE html>
<html>
<body>
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<%!
import random 

r = lambda: random.randint(128,256)

def get_branch_order(BM):
    b_order = []
    for i in range(len(BM.keys())):
        b_order.append('')
    
    for bname in BM:
        idx = BM[bname]['column']
        b_order[idx-1] = bname
    
    #print(BM)
    #print(b_order)
    return b_order

branch_map = {}

%>
 
<style>
<<<<<<< HEAD
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
         <td  style = "border:1px; background-color:lightgray" >${comit_record[i]['branches']}</td>
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
      <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ${comit['author']}</td>
      <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ${comit['datetime']}</td>
      
    </tr>
      %endfor
  </table>
</div>
=======
.circle{
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background-color: blue
}
</style>

<div style="float: left;">

>>>>>>> 7b5bc6c13b924c0901f7d10a253ef31d1964d830

<table cellspacing = 0 > 
%for CR in comit_record:
<!--
{'message': "Merge branch 'FB' of ssh://server.tdea/data/git-repositories/eims-dev   ,
'datetime': datetime.datetime(2013, 1, 17, 18, 10, 51), 'branches': 'FB',
'commit_hash': '6c16190fb1240c6cce0081fde03509a240b6151b',   }
-->

<tr>
  <%
  branch = CR['branches']
  if CR['branches'] not in branch_map:
      branch_map[branch] = {'color': '#%02X%02X%02X' % (r(),r(),r()), 'column': len(branch_map)+1}
  
  %>
  
  <td>${CR['commit_hash']}</td> 
  <td>${CR['message']}</td>
  <td>${CR['datetime']}</td>
  
  %for bname in get_branch_order(branch_map):
    <td style = "width:5px; background-color: ${branch_map[bname]['color']}" >
    %if bname == CR['branches']:
        <div class="circle"></div>
    %endif
    </td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
  %endfor

  
</tr>

%endfor
</table>
</div>
</body>
</html>
      
  
      
  

