Trong mật mã Affine, đầu tiên bảng chữ cái của thông điệp cần mã hóa có kích thước {\displaystyle m} m sẽ được chuyển thành các con số tự nhiên từ {\displaystyle 0..m-1} {\displaystyle 0..m-1}. Sau đó dùng một hàm mô đun để mã hóa và chuyển thành bản mã.

Hàm mã hóa cho một ký tự như sau:

{\displaystyle {\mbox{E}}(x)=(ax+b)\mod {m},} {\displaystyle {\mbox{E}}(x)=(ax+b)\mod {m},}
Với {\displaystyle m} m là kích thước của bảng chữ cái, {\displaystyle a} a và {\displaystyle b} b là khóa mã. Giá trị {\displaystyle a} a được chọn sao cho {\displaystyle a} a và {\displaystyle m} m là nguyên tố cùng nhau. Hàm giải mã là

{\displaystyle {\mbox{D}}(x)=a^{-1}(x-b)\mod {m},} {\displaystyle {\mbox{D}}(x)=a^{-1}(x-b)\mod {m},}
với {\displaystyle a^{-1}} {\displaystyle a^{-1}} là nghịch đảo của {\displaystyle a} a theo mô đun {\displaystyle m} m. Tức là

{\displaystyle 1=aa^{-1}\mod {m}.} {\displaystyle 1=aa^{-1}\mod {m}.}
Nghịch đảo mô đun của {\displaystyle a} a chỉ tồn tại nếu {\displaystyle a} a và {\displaystyle m} m là nguyên tố cùng nhau. Hàm giải mã là hàm ngược của hàm mã hóa:

{\displaystyle {\begin{aligned}{\mbox{D}}({\mbox{E}}(x))&=a^{-1}({\mbox{E}}(x)-b)\mod {m}\\&=a^{-1}(((ax+b)\mod {m})-b)\mod {m}\\&=a^{-1}(ax+b-b)\mod {m}\\&=a^{-1}ax\mod {m}\\&=x\mod {m}.\end{aligned}}} {\displaystyle {\begin{aligned}{\mbox{D}}({\mbox{E}}(x))&=a^{-1}({\mbox{E}}(x)-b)\mod {m}\\&=a^{-1}(((ax+b)\mod {m})-b)\mod {m}\\&=a^{-1}(ax+b-b)\mod {m}\\&=a^{-1}ax\mod {m}\\&=x\mod {m}.\end{aligned}}}
