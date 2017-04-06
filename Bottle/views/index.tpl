<h1>Hello {{name}}</h1>

% if True:
    <h1>If block</h1>
% else:
    <h1>Else Block </h1>
% end

% for i in range(10):
    <p> This is loop idnex: {{i}}</p>
% end