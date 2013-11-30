 
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
   %for branch in branches_names:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${branch}</td>
      </tr>
      %endfor  
  </table>
  ${diagram_record}
   <table>
    <tr class="tr_heading">
      <th>Branch Name</th>
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>Commit Message</th>
    </tr>
    %for commit in comit_record:
      %for j in range(len(commit)):
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${commit[j]['branches']}</td>
      <td>${commit[j]['commit_hash']}</td>
      <td>${commit[j]['author']}</td>
      <td>${commit[j]['datetime']}</td>
      <td>${commit[j]['message'].replace("\n", "<br />\n") | n}</td>
      %endfor
    </tr>
      
    %endfor
  </table>
  
</div>


