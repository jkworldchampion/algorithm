#include <stdio.h>
#include <stdlib.h>

#define MAX_DEGREE 101
#define MAX_TERMS 101
#define SIZEOF(arr) sizeof(arr) / sizeof(*arr)

// polynomial 1 구조체 정의
typedef struct {
    int degree;
    float coef[MAX_DEGREE];
} polynomial_1;

// polynomial 2 구조체 정의
typedef struct {
    float coef_2;
    int expon;
} polynomial_2;

// polynomial 1 출력 함수
void print_poly(polynomial_1 poly){
    for(int i = 0; i <= poly.degree; i++){
        printf("%2.0fx^%d", poly.coef[i], poly.degree-i);  // 예쁘게 출력해주기
        if(i < poly.degree){
            printf(" + ");  // 마지막 항은 + 출력하지 않기
        }
    }
    printf("\n");
}

// polynomial 2 출력 함수
void print_poly_2(polynomial_2 *poly, int size_of_){
    int signal = 0;
    for(int i = 0; i < size_of_; i++){
        if (poly[i].coef_2 == 0){  // 계수가 0일 경우 한번만 출력, 나중에 곱셈 연산을 위해 필요
            signal++;
        }
        if (signal == 1){
            printf("0\n");
            return;
        }
        printf("%2.0fx^%d", poly[i].coef_2, poly[i].expon);  // 출력은 위와 비슷하게
        if(i < size_of_ - 1){
            printf(" + ");
        }
    }
    printf("\n");
}

// polynomial 1 pmult 함수
polynomial_1 pmult(polynomial_1 A, polynomial_1 B){
    polynomial_1 C;
    C.degree = A.degree + B.degree;  // 결과 다항식의 차수는 두 다항식의 차수의 합
    for(int i = 0; i <= C.degree; i++){
        C.coef[i] = 0;   // 결과 다항식의 계수 초기화
    }
    for(int i = 0; i <= A.degree; i++){
        for(int j = 0; j <= B.degree; j++){
            C.coef[i+j] += A.coef[i] * B.coef[j]; // 계수 곱셈 연산 수행, 결과 다항식의 계수에 더하기
        }
    }
    return C;
}

// polynomial 2 pmult 함수
polynomial_2 *pmult_2(polynomial_2 *A, int size_of_A, polynomial_2 *B, int size_of_B){
    polynomial_2 *C = (polynomial_2 *)malloc(size_of_A * size_of_B * sizeof(polynomial_2));  // 결과 다항식을 저장할 배열 동적 할당
    polynomial_2 *result = (polynomial_2 *)malloc(size_of_A * size_of_B * sizeof(polynomial_2));  // 결과 다항식을 정렬할 배열 동적 할당

    // 전체적인 곱셈 연산 수행
    int count = 0;
    for(int i = 0; i < size_of_A; i++){  // A 다항식의 항들을 하나씩 꺼내서 
        for(int j = 0; j < size_of_B; j++){  // B 다항식의 항들과 곱셈 연산 수행
            C[count].coef_2 = A[i].coef_2 * B[j].coef_2;
            C[count].expon = A[i].expon + B[j].expon;
            count++;
        }
    }
    // 결과 다항식을 합하고, 같은 지수를 가진 항들을 합치기
    count = 0;
    for(int i = 0; i < size_of_A * size_of_B; i++){  // 결과 다항식을 하나씩 꺼내서
        int expon = C[i].expon;
        float coef_2 = C[i].coef_2;

        for(int j = i + 1; j < size_of_A * size_of_B; j++){  // 같은 지수를 가진 항들을 찾아서 계수를 합치기
            if(C[j].expon == expon){
                coef_2 += C[j].coef_2;
                C[j].expon = -1;  // 합쳐진 항은 지수를 -1로 바꾸어서 또 더해지지 않게
            }
        }
        if (expon == -1){  // 합쳐진 항은 결과 다항식에 추가하지 않기
            continue;  
        }
        result[count].coef_2 = coef_2;
        result[count].expon = expon;
        count++;
    }
    return result;
}

int main(){
    // A(x) = 3x^3 + 2x^2 + 4, B(x) = x^4 + 10x^3 + 3x^2 + 1
    // polynomial array 1
    polynomial_1 A;
    A.degree = 3;
    A.coef[0] = 3;
    A.coef[1] = 2;
    A.coef[2] = 0;
    A.coef[3] = 4;

    polynomial_1 B;
    B.degree = 4;
    B.coef[0] = 1;
    B.coef[1] = 10;
    B.coef[2] = 3;
    B.coef[3] = 0;
    B.coef[4] = 1;


    // print polynomial 1
    printf("Polynomial Representation 1\n");
    printf("A(x) = ");
    print_poly(A);
    printf("B(x) = ");
    print_poly(B);
    printf("\n");

    // result_poly(x) = A(x) * B(x)
    polynomial_1 result_poly = pmult(A, B);
    printf("Polynomial Multiplication 1\n");
    printf("A(x) * B(x) = ");
    print_poly(result_poly);
    printf("\n\n");

    // C(x) = 2x^1000 + 1, D(x) = X^4 + 10x^3 + 3x^2 + 1
    // polynomial array 2
    polynomial_2 C[2];
    C[0].coef_2 = 2;
    C[0].expon = 1000;
    C[1].coef_2 = 1;
    C[1].expon = 0;

    polynomial_2 D[4];
    D[0].coef_2 = 1;
    D[0].expon = 4;
    D[1].coef_2 = 10;
    D[1].expon = 3;
    D[2].coef_2 = 3;
    D[2].expon = 2;
    D[3].coef_2 = 1;
    D[3].expon = 0;

    // print polynomial 2
    printf("Polynomial Representation 2\n");
    printf("C(x) = ");
    print_poly_2(C, SIZEOF(C));
    printf("D(x) = ");
    print_poly_2(D, SIZEOF(D));
    printf("\n");

    // result_poly_2(x) = C(x) * D(x)
    printf("Polynomial Multiplication 2\n");
    polynomial_2 *result_poly_2 = pmult_2(D, SIZEOF(D), C, SIZEOF(C));
    printf("C(x) * D(x) = ");
    print_poly_2(result_poly_2, SIZEOF(D) * SIZEOF(C));
    printf("\n\n");

    free(result_poly_2);


    // 출력이 잘 되는 것을 보았으니, 이제 다른 test case를 만들어서 출력하기
    printf("Test Case 2\n");
    polynomial_1 test_1;
    test_1.degree = 4;
    test_1.coef[0] = 8;
    test_1.coef[1] = 0;
    test_1.coef[2] = -3;
    test_1.coef[3] = 3;
    test_1.coef[4] = 1;

    polynomial_1 test_2;
    test_2.degree = 4;
    test_2.coef[0] = 4;
    test_2.coef[1] = 8;
    test_2.coef[2] = 3;
    test_2.coef[3] = 3;
    test_2.coef[4] = 5;

    printf("Polynomial Representation 1\n");
    printf("test_1(x) = ");
    print_poly(test_1);
    printf("test_2(x) = ");
    print_poly(test_2);
    printf("\n");
    printf("Polynomial Multiplication: ");
    polynomial_1 test_case_result_1 = pmult(test_1, test_2);
    print_poly(test_case_result_1);
    printf("\n\n");

    polynomial_2 test_3[4] = {
        {2, 4},
        {-1, 3},
        {4, 2},
        {1, 0}
    };

    polynomial_2 test_4[4] = {
        {1, 3},
        {10, 2},
        {-3, 1},
        {1, 0}
    };
    printf("Polynomial Representation 2\n");
    printf("test_3(x) = ");
    print_poly_2(test_3, SIZEOF(test_3));
    printf("test_4(x) = ");
    print_poly_2(test_4, SIZEOF(test_4));
    printf("\n");
    printf("Polynomial Multiplication: ");
    polynomial_2 *test_case_result_2 = pmult_2(test_3, SIZEOF(test_3), test_4, SIZEOF(test_4));
    print_poly_2(test_case_result_2, SIZEOF(test_3) * SIZEOF(test_4));


    return 0;
}
