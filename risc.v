module simple_risc_processor (
    input clk,
    input reset,
    input [31:0] data_in,
    output reg [31:0] data_out
);

    // Assert that data_out is always data_in + 1
    assert property (@(posedge clk) reset || (data_out == (data_in + 1)))
        else $fatal("Assertion failed: data_out is not data_in + 1");

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            data_out <= 32'b0;
        end else begin
            data_out <= data_in + 1;
        end
    end
endmodule
