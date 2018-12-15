import solid
import solid.utils

cube = solid.utils.up(100)(
     solid.cube(10)
)




kugle = solid.sphere(10)

cyl = solid.cylinder(r=20, h=2)

sum = cyl + kugle + cube

solid.scad_render_to_file(sum,'../ZZ3DModels/Mirsad3D.scad')

