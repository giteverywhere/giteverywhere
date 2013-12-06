<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing current branch of repository: ${repository_name}</h1>
  
  <table>
    <tr class="tr_heading">
      <th>Branch name</th>
    </tr>
    
%if output == 'html':
   %for branch in branch_view:
     <tr class="${loop.cycle('oddrow', 'evenrow')}">
        <td>${branch['branch_name']}</td>
      </tr>
   %endfor  

%elif output == 'json':
      <tr>
        <td>${data}</td>
      </tr>  

%endif 
  </table>
</div>








 
 
 
 
    

   
   
 
