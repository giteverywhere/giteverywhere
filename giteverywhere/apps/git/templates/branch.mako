<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing branch view of repository: ${repository_name}</h1>

  <table>
    <tr class="tr_heading">
      <th>Branch name</th>
     
    </tr>
 
   %for branch in branches:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${branch}</td>
      </tr>
      %endfor  
  </table>
  
</div>









 
 
 
 
    

   
   
