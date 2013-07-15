<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  
  
  <table>
    <tr class="tr_heading">
      <th>Id</th>
      <th>Name</th>
    </tr>

      <td><a href="${request.route_url('git.branch')}">Branches</a></td>
      
    </tr>
 
  </table>
  
</div>



    
    
