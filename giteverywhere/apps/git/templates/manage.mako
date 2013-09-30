<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Branches</h1> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 
  
     <a href ="${request.route_url('git.clog', repo=repo)}">Commits</a>&nbsp;&nbsp;&nbsp;&nbsp;

     <a href="${request.route_url('git.branch', repo=repo)}">Branches</a> &nbsp;&nbsp;&nbsp;&nbsp;
    
     <a href="${request.route_url('git.tag', repo=repo)}">Tags</a> &nbsp;&nbsp;&nbsp;&nbsp;
     
     <a href="${request.route_url('git.diff', repo=repo)}">Difference</a>&nbsp;&nbsp;&nbsp;&nbsp;
     
     <a href="${request.route_url('git.files', repo=repo)}">List</a>&nbsp;&nbsp;&nbsp;&nbsp;
     
     
       

  <table>
    <tr class="tr_heading">
    
      <th>Branch name</th>

    </tr>
   %for branch in branch_view:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${branch['branch_name']}</td>
   
      %endfor 
 
   
  </table>
  <h1>First/most recent commit in ${repo}  : </h1>&nbsp;&nbsp;&nbsp;&nbsp;
  <table>
    <tr class="tr_heading">
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>Commit Message</th>
    </tr>
    %for commit in comit_log:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${commit['commit_hash']}</td>
      <td>${commit['author']}</td>
      <td>${commit['datetime']}</td>
      <td>${commit['message'].replace("\n", "<br />\n") | n}</td>
    </tr>
    %endfor
     
  </table>
  
   
  
  
  

  

  
</div>