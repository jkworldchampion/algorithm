#include <stdio.h>
#include <stdlib.h>

#define MAX_DEGREE 101
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// 다항식 구조체 정의
typedef struct {
    int degree;
    float coef[MAX_DEGREE];
} Polynomial;

// 다항식 출력 함수
void printPolynomial(Polynomial poly) {
    for (int i = 0; i <= poly.degree; i++) {
        printf("%2.0fx^%d", poly.coef[i], poly.degree - i);
        if (i < poly.degree) {
            printf(" + ");
        }
    }
    printf("\n");
}

// 다항식 덧셈 함수
Polynomial addPolynomials(Polynomial poly1, Polynomial poly2) {
    Polynomial result;
    int max_degree = (poly1.degree > poly2.degree) ? poly1.degree : poly2.degree;
    result.degree = max_degree;
    
    // 각 차수에 해당하는 계수를 더함.
    for (int i = 0; i <= max_degree; i++) {
        result.coef[i] = ((i <= poly1.degree) ? poly1.coef[i] : 0) + ((i <= poly2.degree) ? poly2.coef[i] : 0);
    }

    return result;
}

// 다항식 곱셈 함수
Polynomial multiplyPolynomials(Polynomial poly1, Polynomial poly2) {
    Polynomial result;
    result.degree = poly1.degree + poly2.degree;

    // 다항식 초기화
    for (int i = 0; i <= result.degree; i++) {
        result.coef[i] = 0;
    }   

    if (poly1.degree == 0 && poly2.degree == 0) {
        result.coef[0] = poly1.coef[0] * poly2.coef[0];
        return result;
    }

    if (poly1.degree == 0 || poly2.degree == 0) {
        Polynomial nonZeroPoly = (poly1.degree == 0) ? poly2 : poly1;
        Polynomial zeroPoly = (poly1.degree == 0) ? poly1 : poly2;

        for (int i = 0; i <= nonZeroPoly.degree; i++) {
            result.coef[i + zeroPoly.degree] = nonZeroPoly.coef[i] * zeroPoly.coef[0];
        }

        return result;
    }

    int halfDegree = (poly1.degree > poly2.degree) ? poly1.degree / 2 : poly2.degree / 2;

    Polynomial poly1Low, poly1High, poly2Low, poly2High;
    poly1Low.degree = poly2Low.degree = halfDegree;
    poly1High.degree = poly1.degree - halfDegree - 1;
    poly2High.degree = poly2.degree - halfDegree - 1;

    for (int i = 0; i <= poly1Low.degree; i++) {
        poly1Low.coef[i] = poly1.coef[i];
        poly1High.coef[i] = poly1.coef[i + halfDegree + 1];
    }

    for (int i = 0; i <= poly2Low.degree; i++) {
        poly2Low.coef[i] = poly2.coef[i];
        poly2High.coef[i] = poly2.coef[i + halfDegree + 1];
    }


    Polynomial z0 = multiplyPolynomials(poly1Low, poly2Low);
    Polynomial z1 = multiplyPolynomials(addPolynomials(poly1Low, poly2High), addPolynomials(poly2Low, poly1High));
    Polynomial z2 = multiplyPolynomials(poly1High, poly2High);

    Polynomial temp = addPolynomials(z0, z2);

    for (int i = 0; i <= temp.degree; i++) {
        z1.coef[i] -= temp.coef[i];
    }

    for (int i = 0; i <= z0.degree; i++) {
        result.coef[i] = z0.coef[i];
    }

    for (int i = 0; i <= z1.degree; i++) {
        result.coef[i + halfDegree + 1] += z1.coef[i];
    }

    for (int i = 0; i <= z2.degree; i++) {
        result.coef[i + 2 * halfDegree + 2] += z2.coef[i];
    }

    return result;
}

int main() {
    Polynomial poly1, poly2;

    // 첫 번째 다항식 초기화
    poly1.degree = 3;
    poly1.coef[0] = 10;
    poly1.coef[1] = 6;
    poly1.coef[2] = 8;
    poly1.coef[3] = 4;

    // 두 번째 다항식 초기화
    poly2.degree = 3;
    poly2.coef[0] = 5;
    poly2.coef[1] = 6;
    poly2.coef[2] = 7;
    poly2.coef[3] = 8;

    // 첫 번째 다항식 출력
    printf("First polynomial:\n");
    printPolynomial(poly1);

    // 두 번째 다항식 출력
    printf("Second polynomial:\n");
    printPolynomial(poly2);
    printf("\n");

    // 다항식 덧셈 수행
    Polynomial sum = addPolynomials(poly1, poly2);
    printf("Result of polynomial addition:\n");
    printPolynomial(sum);
    printf("\n");

    // 다항식 곱셈 수행
    Polynomial result = multiplyPolynomials(poly1, poly2);

    // 결과 출력
    printf("Result of polynomial multiplication:\n");
    printPolynomial(result);

    return 0;
}
