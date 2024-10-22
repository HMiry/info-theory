v(1) = input("Value of the first feature\n");
v(2) = input("Value of the second feature\n");
v(3) = input("Value of the thrid feature\n");
if v(1) > 30
    class = 1
else
    if v(2) == 0
        class = 0
    else
        if v(3) < 40
            class = 1
        else
            class = 0
        end
    end
end