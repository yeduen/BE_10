# main.py

# oz_package 패키지의 oz_module_1 모듈을 'one'이라는 별칭으로 임포트합니다.
import oz_package.oz_module_1 as one

# oz_package 패키지의 oz_module_2 모듈을 'two'라는 별칭으로 임포트합니다.
import oz_package.oz_module_2 as two

print(one.val_1)
print(two.val_2)
