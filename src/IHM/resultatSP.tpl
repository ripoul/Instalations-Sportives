<h1>Resultat</h1>
<form action="http://localhost:9999/" methode="GET">
<INPUT TYPE="submit" NAME="nom" VALUE="Nouvelle recherche">
</FORM>

<table>
<tr><th>Activité</th><th>Nom equipement</th><th>Nom installation</th><th>Adresse</th><th>CP</th><th>Ville</th><th>Map</th></tr>
%for row in rows:
    <tr>
    
        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
    
    <td><a href="http://localhost:9999/installation/map?lat={{row[6]}}&long={{row[7]}}&ref={{row[5]}}"}> Map</a></td>
    </tr>
%end
</table>