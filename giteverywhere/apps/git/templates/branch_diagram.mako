
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
   
    return b_order

branch_map = {}

%>

<style>

.circle{
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background-color: blue
}


</style>

<div style="float: left;">
<table cellspacing = 0 > 
<tr class="tr_heading">
      <th>Commit Hash</th>
      <th>Commit Message</th>
      <th>Date & Time</th>
      <th>Branch</th>
</tr>

%for CR in sorted_record:
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
    
  <td>&nbsp;${CR['commit_hash']}</td> 
  <td>&nbsp;&nbsp;&nbsp;${CR['message']}</td>
  <td>&nbsp;&nbsp;&nbsp;${CR['datetime']}&nbsp;&nbsp;</td>
  <td>&nbsp;&nbsp;&nbsp;${CR['branches']}&nbsp;&nbsp;</td>
  <td>&nbsp;&nbsp;&nbsp;${CR['is_first']}&nbsp;&nbsp;</td>
  <td>&nbsp;&nbsp;&nbsp;${CR['is_last']}&nbsp;&nbsp;</td>
 
  %for bname in get_branch_order(branch_map): 
    <td style = "width:5px; background-color: ${branch_map[bname]['color']}" >
    
    %if bname == CR['branches']:     
        <div class="circle"></div>        
    %endif
      <%
      if CR['branches'] == bname:
        if CR['is_first'] == 'TRUE': 
          branch_map[bname]['color'] = 'white'
        endif
      endif
   %> 
    <td>&nbsp;</td>  
  %endfor          
   
%endfor
</tr> 
</table>
</div>
</body>
</html>
    